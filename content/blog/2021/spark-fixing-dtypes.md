+++
title = "Fixing Spark Datatypes"
date = "2021-08-29"
categories = [ "thoughts" ]
tags = ["spark", "python"]
+++

You can't always control what your upstream data produce will change
<!--more-->

I ran into an interesting [software contract](https://martinfowler.com/articles/consumerDrivenContracts.html) issue a few years
ago where upstream data pipelines producing parquet and avro files were tweaking their outputs often. This was usually fine as
they were mostly just adding new columns to the data. However, they weren't versioning these changes, so a change could
come at any moment and occasionally it would include a schema change.

A certain column that was a string might become an integer and all of a sudden everything I was doing would break. Given the nature of
my work, I couldn't just make a minor tweak to the schema on my end and deploy again to production. A lot of what I was doing
required consuming the last X months of data. Asking Spark to ingest all of that at once would often result in a schema mismatch
error due to a change event. Waiting months for the data to clear out was not an option.

So. . .I wrote what would eventually become the core feature of a pip installable python library focused on solving problems where 
Spark code meets other systems (S3, Postgres, API network calls, etc). 

The crown jewel of that library was a Spark load function that would detect a schema change, find it, load in the data before and
after as separate dataframes, and then union them after casting the old datatypes to match the new ones.

It worked well, but could only handle a single schema change event. I finally found some time to write a new (experimental) version 
that can do this not just for a single schema change event, but any number of them.

Enough talk. . .lets code.

{{< highlight python "linenos=table" >}}
def spark_read(files_list):
  # Does all the magic to load data into spark
  # specifically parquet vs avro vs CSV specific settings
  # This expects options like:
  # format, columns, delimiter, headers
  pass
{{< / highlight >}}

Above is just a stub function. This is for normal spark load steps that will be specific to your situation. Since that can be a
lot of code and differ greatly per situation, I abstracted it here to make the below functions more obvious to read.

{{< highlight python "linenos=table" >}}
def binary_search(files_list, dtypes):
  left_idx = 1
  right_idx = len(files_list) - 1
  while left_idx < right_idx:
    mid = left_idx + round((right_dx - left_idx)/2)
    mid_dtypes = spark_read(files_list(mid)).dtypes
    if mid_dtypes == dtypes:
      # Same as target, ignore right half
      right_idx = mid
    else:
      # dtypes differ, so ignore left half
      left_idx = mid + 1
  # When left meets right, we have converged on the moment of change
  return (files_list[:left_idx], files_list[left_idx:])
{{< / highlight >}}

The argument **dtypes** is the desired datatypes we are want. In my case, I assume the newer schema is better.
This [binary search](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search) function
efficiently finds the first file that has the newer schema. The function returns two lists, the first is all older files (which
might have multiple schema change events btw) and the second has all files containing the desired schema.

{{< highlight python "linenos=table" >}}
def fix_dtypes(loaded_dfs):
  final_df = loaded_dfs.pop(-1)
  for df in loaded_dfs[::-1]:
    # If we have more than one df (e.g. schema changes)
    # loop backwards in time and attempt to enrich/improve and join older data.
    try:
      for column, dtype in final_df.dtypes:
        df = df.withColumn(column, df[column].cast(dtype))
      final_df = final_df.unionByName(df)
    except Exception:
      # Likely some old data differs too drastically from current good data
      break
  return final_df
{{< / highlight >}}

The **fix_dtypes()** function takes a list of dataframes. The last one in the list is the "good" one that has the newest schema we
trust. We loop over the other dataframes, starting with the newest one, and attempt to cast it's schema and union the data in to
the single final dataframe. We keep going further back in time until all the data is merged or we hit a dataframe that has such a
diverging schema that we can't union it. If that happens, we just return all the data that we were able to fix.

{{< highlight python "linenos=table" >}}
def spark_load(files):
  loaded_dfs = []
  dtypes = spark_read(files[-1]).dtypes
  try:
    df = spark_read(files)
    loaded_dfs.insert(0, df)
  except Exception:
    for part in binary_search(files, dtypes)[::-1]:
      loaded_dfs.insert(0, spark_load(part))
  return fix_dtypes(loaded_dfs)
{{< / highlight >}}

Now we can bring it all together. We first try a naive load to be efficient. If it succeeds we return early. Note that 
**fix_dtypes()** ends up doing nothing if it's given only one df.

If we get an exception, we break the files intelligently into two chunks by finding a schema difference. The second chunk has
newer files. We call **spark_load()** again for each chunk. This will keep happening recursively until we finally
get a clean load of data like the happy path above.

We then do the same for all sub-chunks of files. As the recursive calls propagate back up, older data will slowly get union-ed
into newer data.

### Potential Bugs
If the schema is changed but then changed back soon after, this might cause a problem during the binary search. I haven't tested
this situation, but I'm pretty sure it would still work, but might get stuck doing a lot of binary searches until it can finally
load a df without error. The final **fix_dtypes()** step would then have a lot of dfs to union.

There also might be an issue of a middle chunk load failing but older loads succeeding. If this happens then we could end up with a
final df missing a chunk of data in the middle. The solution is probably to short circuit out of all the recursion and return only
what we've loaded up to that point.

Also, you may want to be careful blindly casting data like this. Depending on your situation you might WANT to fail instead so
you don't ingest poorly published data. At a minimum, you should probably add some alerting to this code so you are aware of data
issue that might need investigation.

### Future Improvements
As I said at the beginning, this is experimental code because I'm not working with Spark at the moment. I'm sure there are one or
two bugs hiding here that I would like to fix.

Also, it might be nice to create a lookup dictionary of "acceptable schema changes" and have that enforced during **fix_dtypes()**.
That way any unsafe casting (ex: you've decided that you want float -> double treated as an exception instead) can be passed as
configuration so this tool only handles situations you trust. That way the default behavior is to fail. After an investigation is
done and a certain schema change is considered acceptable, the logic could then be updated by adding a line of configuration.

Another form of this would be to pass it a list of dates via config. Each date being a known schema change event that caused a
problem and that has been considered safe to fix automatically.

The above two features could be combined to make this a very flexible and powerful tool. I never came across those situations for
myself and so decided to not add the complexity.

### Final Thoughts
If you search this problem online you'll find a lot of people saying "just go fix your data". This is true. If you can, you should
fix the data so you don't have to deal with all of this and avoid other data issues. But if you don't control that data or are otherwise unable to fix it, then I hope these code snippets find you well.
