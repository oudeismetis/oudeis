+++
title = "Spark JDBC Throttling, Part 2"
date = "2020-08-12"
categories = [ "thoughts" ]
image = "img/foo.jpeg"
showonlyimage = false
draft = true
+++

Again...Spark will hammer the relational DB you connect to if you let it.
<!--more-->

Recently I wrote about solving a problem with Spark [hammering a DB]({{< ref "spark-jdbc-throttling.md" >}}).

That initial problem occurred when trying to download too much data too quickly from a relational DB. Spark always wants to do things fast and can overwhelm a DB with too many connections.

But what about a similar problem while writing to the DB?

So you want to write a large df from spark into a relational DB, but spark keeps overwhelming the DB on you.
You aren't given many settings in `spark.write.jdbc()`. Most of the connection settings are set deep within spark where you can't touch them.
Again...spark is designed to do a lot of operations very fast, so it will hit the DB as hard as it can without thinking twice.
So....you basically can't use spark to do this.
Also...you can't do it outside of spark as loading millions of rows into a Python data structure is a bad idea.

What to do?

The hack solution is to chunk the dfs and rely on spark overhead to slow things down enough for PG to be happy.
While you're at it, setting `numPartitions` and `batchsize` to be suitably low will also help. Between the three knobs you can turn, you can slow spark up enough to get the job done.
Also while you are at it, temporarily turning off read replication and indexes on the table will of course also help.
Writing to a temporary table with everything turned off, then sending a regular command to PG to update or insert using another table will give PG the best opportunity to optimize things itself.

A better solution I didn't try...
Write out to a file on the HDFS. Then use psycopg2 or psql as normal, but inserting from a file. This will solve the local memory issues by keeping the bulk of the data inside spark, but also let you tune your PG call with a connection pool, CopyManager, or whatever other settings you want to set up to write in a controlled way.
{{< highlight python "linenos=table" >}}
for df_part in df_in_chunks(df, 500000):
    df_part.write.format('jdbc') \
                 .mode('append') \
                 .option('driver', 'org.postgresql.Driver') \
                 .option('dbtable', table_name) \
                 .option('batchsize', 40) \
                 .option('numPartitions', 1) \
                 .option('user', user) \
                 .option('password', password) \
                 .save()
{{< / highlight >}}

## chunking a df
In spark you generally want to keep all operations inside of spark as performance is better.
But sometimes you need to write to a DB where you are worried about spiking the IOPS.
Or you need to call an API (and maybe that API call can only happen once)
Or you need to do some other sort of weird operation that you can't do directly in spark and can't solve with a UDF or other solution.
Bringing too much data in a Python data structure could crash things or bog them down.
Or maybe you are working on sooooo much data that if/when an operation errors you want to pick up where you left off on the next run.
So....lets operate in chunks.

{{< highlight python "linenos=table" >}}
def df_in_chunks(df):
    """
    in: df
    out: [df1, df2, ..., df100]
    """
    count = df.count()

    if count > row_count:
        num_chunks = count//row_count
        chunk_percent = 1/num_chunks  # 1% becomes 0.01
        return df.randomSplit([chunk_percent]*num_chunks, seed=1234)
    return [df]

{{< / highlight >}}
