+++
title = "Spark jdbc Throttling"
date = "2020-04-16"
showonlyimage = false
+++

Spark will hammer the relational DB you connect to if you let it.
<!--more-->

I ran into an issue with Spark recently where the database I was reading and writing to was experiencing CPU spiking issues.

This is an obvious issue on the face of it, since Spark will use every resource it has available in your cluster to do any task you ask it to. You can and should configure the database to throttle connections, but ideally there would also be a setting for spark’s use of jdbc that would allow you to throttle the number of concurrent connections. Sadly there does not appear to be one.

Alternatively, having the ability to increase/decrease Spark resources within the same SparkContext would also solve the problem. 

Here there is a ray of hope as you can edit Spark’s resources like this:

{{< highlight python "linenos=table" >}}
max_cores = spark.conf.get('spark.executor.cores')
conf = spark.sparkContext._conf.set('spark.executor.cores', 5)
spark.sparkContext.stop()
spark = SparkSession.builder.config(conf=conf).getOrCreate()
{{< / highlight >}}

And this works, unfortunately you now have a new spark context, which means any previously loaded dataframes are lost.

This is a [known issue](https://issues.apache.org/jira/browse/SPARK-8008). I think one commenter said it best:
```
Too bad that this issue is not considered high priority. Too many times I come to the problem that I need to process billions of records. So the only way to handle this is to create a huge amount of partitions, and then throttle using spark.executor.cores. However this setting effectively throttles my entire RDD, not just the portion that loads from database. It would be hugely beneficial that I can not only restrict the number of partitions at any time, but also the task concurrency at any point in my RDD.
```

There may be a way around this by staging data in HDFS or local FS and reloading it, but the prospects of investigating that weren’t appealing for the problem I was solving.

So I was forced to artificially limit the amount of work Spark would take on, and thus limit the resources Spark would use to connect to the DB.

The simpler solution is to use numPartitions to determine the number of chunks Spark should break the read up with.

But in my case my index column wasn't evenly distributed so doing that would result in a single DB connection attempting to download all the data. (Can't have nice things)

Instead, for my particular sitation, I had to manually define the partitions by passing a list of predicates.

{{< highlight python "linenos=table" >}}
pg_url = f'jdbc:postgresql://{url}:5432/{database}'
config = {
    'user': 'foo',
    'password': 'bar',
    'driver': 'org.postgresql.Driver'
}

# The index column here is uneven
# Manually build our chunks of work.
predicates = [
    'id < 100',
    'id >= 100 AND id < 1000',
    'id >= 1000 AND id < 4000',
    'id >= 4000']

# Spark will still read in parallel,
# but will max out at len(predicates) number of DB connections
df = spark.read.jdbc(url=pg_url, table='foo',
                     predicates=predicates, properties=config)
{{< / highlight >}}

This is a simple toy example that results in Spark only opening X connects to the DB. Not the most robust solution, but it worked.


### Links:
 * https://issues.apache.org/jira/browse/SPARK-8008
 * https://stackoverflow.com/questions/41886346/spark-2-1-0-session-config-settings-pyspark



