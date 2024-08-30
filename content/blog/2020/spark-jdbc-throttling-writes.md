+++
title = "Spark JDBC Throttling, Part 2"
date = "2020-09-04"
categories = [ "thoughts" ]
tags = ["spark", "python"]
showonlyimage = false
+++

Again. . .Spark will hammer a relational DB you connect to if you let it.
<!--more-->

Recently I wrote about solving a problem with Spark [hammering a database]({{< ref "spark-jdbc-throttling.md" >}}).

That initial problem occurred when trying to download too much data too quickly from a relational DB. Spark always wants to do things fast and can overwhelm a DB with too many connections.

But what about a similar problem while writing to the database?
There are three main places you can alter configuration to solve this issue (or at least mitigate and alleviate).

### Spark
Again. . .spark is designed to do a lot of operations very fast, so it will hit the DB as hard as it can without thinking twice and doesn't offer any direct settings for throttling JDBC connections.

However, there are a couple of settings you can pass that will artificially slow things.

{{< highlight python "linenos=table" >}}
df.write.format('jdbc') \
        .mode('append') \
        .option('driver', 'org.postgresql.Driver') \
        .option('dbtable', table_name) \
        .option('batchsize', 40) \
        .option('numPartitions', 1) \
        .option('rewriteBatchedInserts', True) \
        .option('user', user) \
        .option('password', password) \
        .save()
{{< / highlight >}}

**batchsize** will force Spark to spend more time sending data over the network as this limits how many rows Spark will send to the DB with each call. Usually you will see recommendations to increase it above the default of 1000 in order to increase the speed at which Spark writes to the DB. But here we want it lowered of course.

**numPartitions** will limit how Spark chops up the work between all the workers/CPUs it has in the cluster. If you set this to a higher number you can end up with 100+ simultaneous connections to the DB. By setting it to 1, we can keep that from happening.

**rewriteBatchedInserts** is just a general postgres performance optimization flag. I couldn't find out much about it except that it ["provides 2-3x performance improvement"](https://jdbc.postgresql.org/documentation/head/connect.html#connection-parameters).
### Network Infrastructure
In my case I was running on AWS EMR. There are a couple of things you can optionally do here to help your situation.

* Shrink the number of workers in your cluster (Not an option for me)
* Shrink the size of the machines you are using (Not an option for me)
* Switch to a machine type that is. . .say. . .optimized for memory but weaker on networking

This is something in my case I didn't get time to experiment with, but will be testing in the coming weeks. Just like changing some of the configs above, this is kind of a hack in that we aren't able to directly throttle what Spark is doing, but instead are merely constraining it's resources to force it to slow down.


### Database
There are a number of settings on the database side that you can do to limit the number of connections and how much data those connections can send.

In my case I didn't have the option of tweaking the DB. I was also just more intrigued about what I could do from the Spark side to force it to slow down given that there are many other situations (APIs as one example) where you might want to throttle Spark. Exploring that was interesting to me.

Also, when doing an UPDATE or DELETE from Spark, you should NEVER update the table directly, but instead INSERT to a temporary table where you have disabled indexes, replication, etc first. Then have Spark Update/Delete the main table using the rows from the temp table.

### Conclusion
Throttling Spark is like trying to rein in a horse.

By default Spark really doesn't want you to do it. That makes sense philosophically when you think about the job Spark is meant to do vs what we typically ask other Python application to do.

I've only had a couple of brief opportunities recently to dive into this topic and I don't think I have done it justice yet.

I'm confident there is a good best practice or design pattern for this.

Perhaps stage the data as parquet/avro files in an S3 bucket and have a separate non-spark process consume that data for API/DB operations?

Maybe write out the dataframe in chunks to HDFS and have a separate psycopg2/psql script running to insert into the database while Spark continues to work on other jobs?

I'm sure I'll have more concrete things to say about this topic in the future.

### Links I found useful

* https://www.psycopg.org/docs/pool.html?highlight=pool
* https://stackoverflow.com/questions/39396886/spark-write-to-postgres-slow
* https://forums.databricks.com/questions/8946/writing-dataframe-to-postgresql-via-jdbc-extremely.html
* https://gist.github.com/longcao/bb61f1798ccbbfa4a0d7b76e49982f84
* https://stackoverflow.com/questions/36912442/low-jdbc-write-speed-from-spark-to-mysql
* https://stackoverflow.com/questions/2993251/jdbc-batch-insert-performance/10617768#10617768
* https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html
* https://forum.cockroachlabs.com/t/not-getting-high-enough-write-speeds-but-there-is-no-resource-bottleneck/2747/2
* https://github.com/cockroachdb/docs/issues/3578
* https://stackoverflow.com/questions/30983982/how-to-use-jdbc-source-to-write-and-read-data-in-pyspark
* https://spark.apache.org/docs/latest/api/python/pyspark.sql.html?highlight=jdbc#pyspark.sql.DataFrameWriter
* https://stackoverflow.com/questions/17559300/copy-command-with-psycopg2-library
