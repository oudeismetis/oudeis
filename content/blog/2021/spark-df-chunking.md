+++
title = "Chunking PySpark Dataframes"
date = "2021-01-18"
categories = [ "thoughts" ]
tags = ["spark", "python"]
showonlyimage = false
+++

For when you need to break a dataframe up into a bunch of smaller dataframes
<!--more-->

Spark dataframes are often very large. Far to big to convert to a vanilla Python data structure.

Where possible, you should avoid pulling data out of the JVM and into Python, or at least do the operation with a UDF. But sometimes (possibly because you are short on time) the only solution to your problem is to take your data out of the HDFS and do regular Python operations.

For toy data this is straight forward, but what do you do when you run big data through this code and start running into memory issues?

In my case, I needed to do a slow network call operation. It would take hours and hours to run and if (when) it failed, an atomic transaction would fail and the next run would try to do ALL of it over again from scratch. So my temporary solution (while working on a better Spark-based solution) was to simply chop the work up and save progress periodically so only a small amount of work would need to be reprocessed after a failure.

## Chunking a df
So....lets operate in chunks.

{{< highlight python "linenos=table" >}}
def df_in_chunks(df, row_count):
    """
    in: df
    out: [df1, df2, ..., df100]
    """
    count = df.count()

    if count > row_count:
        num_chunks = count//row_count
        chunk_percent = 1/num_chunks  # 1% would become 0.01
        return df.randomSplit([chunk_percent]*num_chunks, seed=1234)
    return [df]
{{< / highlight >}}

...and how it might be called:

{{< highlight python "linenos=table" >}}
for df_part in df_in_chunks(df, 50000):
    rows = list(map(lambda row: row.asDict(), df_part.collect()))
    do_operation(rows)
    # DON'T DO THIS - See explanation below
    save_progress(df.agg({'id': 'max'}).collect()[0]['max(id)'])
{{< / highlight >}}

The function `df_in_chunks()` take a dataframe and a count for roughly how many rows you want in every chunk. I say "roughly" because `randomSplit()` does not guarantee the count, so a given chunk may have ~1% more rows or fewer rows. Splitting hairs aside, it will return a list of dfs of roughly equal size.

Note that as the name implies, `randomSplit()` does not guarantee order either so you cannot assume that df1 contains the first elements from the parent dataframe sadly. So in the code above, we might be tempted to save off the value of the maximum row id so we can pick up where we left off, but that won't work.

In my case I already had logic to remove rows that already existed in another dataframe, one where the slow operation had already completed successfully. Thus in the event of a failure, rerunning the job would result in fewer rows being processed, and so all of the work would get done eventually. 

As a final thought:

Again...this isn't going to be the fast and performant solution. But this is a nice tool to have in your toolbox, especially when working at the intersection of Spark and other (slower) applications. 
