+++
title = "Spark Fixing Dtypes"
date = "2019-02-28"
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
