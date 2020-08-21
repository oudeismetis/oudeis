+++
title = "Spark Fixing Dtypes"
date = "2020-08-12"
showonlyimage = false
draft = true
+++

"Start with why"
<!--more-->


{{< highlight python "linenos=table" >}}
old_files = []
new_files = []
left_idx = 0
right_idx = len(all_files) - 1

# Newest file has the data types we want
dtypes = spark.read.load(all_files[-1], format=format).dtypes
# Oldest file might be out of sync with our data types
old_dtypes = spark.read.load(all_files[0], format=format).dtypes

if dtypes == old_dtypes:
    # data types haven't changed. Just load all files
    new_files = all_files
else:
    # Do a binary search to find when the data types changed
    while left_idx <= right_idx:
        mid = left_idx + round((right_idx - left_dx)/2)
        mid_dtypes = spark.read.load(all_files[mid], format=format).dtypes

        if mid_dtypes == dtypes:
            right_idx = mid - 1
        else:
            left_idx = mid + 1
    # When left meets right, we have converged on the moment of change
    old_files = all_files[:left_idx]
    new_files = all_files[left_idx:]

df = spark.read.load(new_files, format=format).select(columns_list)
if old_files:
    # Load the older data and cast it's data types before joining everything
    new_df = spark.read.load(old_files, format=format).select(columns_list)
    for column, dtype in dtypes:
        new_df = new_df.withColumn(column, new_df[column].cast(dtype))
    df = df.union(new_df)
{{< / highlight >}}








What to do?

The hack solution is to chunk the dfs and rely on spark overhead to slow things down enough for PG to be happy.
While you're at it, setting `numPartitions` and `batchsize` to be suitably low will also help. Between the three knobs you can turn, you can slow spark up enough to get the job done.
Also while you are at it, temporarily turning off read replication and indexes on the table will of course also help.
Writing to a temporary table with everything turned off, then sending a regular command to PG to update or insert using another table will give PG the best opportunity to optimize things itself.

A better solution I didn't try...
Write out to a file on the HDFS. Then use psycopg2 or psql as normal, but inserting from a file. This will solve the local memory issues by keeping the bulk of the data inside spark, but also let you tune your PG call with a connection pool, CopyManager, or whatever other settings you want to set up to write in a controlled way.


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

for df_part in df_in_chunks(df, 500000):
    df_part.write.format('jdbc').write()
{{< / highlight >}}
