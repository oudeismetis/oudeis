+++
title = "Update PySpark dataframe from a dictionary"
date = "2020-08-14"
categories = [ "thoughts" ]
tags = ["spark", "python"]
showonlyimage = false
+++

I was in a situation a while back where I needed to make an API call to clean up some data in a dataframe. Here is the approach I took.

<!--more-->



- Get all the distinct values for the particular column out of the df
- Make multithreaded and batched calls to the API (important for dealing with a LOT of data)
- Add a new column to the df with the results added

Here is what a sample of that looks like in code

{{< highlight python "linenos=table" >}}
from pyspark.sql.functions import col, udf

def update_from_dict(my_dict):
    def _in_dict(col, my_dict):
        return my_dict(col, 0)
    return udf(lambda l: _in_dict(l, my_dict))

# this is slow
elements = [i[elem] from i in df.select(col_name).distinct().collect()]
results = call_api(elements)
df = df.withColumn(col_name, update_from_dict(results)(col(col_name)))
{{< / highlight >}}

# Performance issues?

Absolutely. Any time you are pulling data out of HDFS, out of JVM, and into Python you incur a cost. Here we are using a [UDF](https://spark.apache.org/docs/latest/api/python/pyspark.sql.html?highlight=udf#pyspark.sql.functions.udf) (User Defined Function) to access the dictionary results for every row in the dataframe.

When at all possible, you should avoid using UDFs and try to keep as much logic as you can in Spark.

# Other Solutions

You could use a UDF to have Spark directly call the API for you. I originally had the code doing this, but it was calling the API for one row at a time, which was taking FOREVER.

So I went with a solution where I could make bulk calls and multithreaded calls to speed things up. 
There might be a way to do that directly from Spark without a UDF, but I never got around to investigating that.

# Final thought/wisdom

I often find that making things go fast is just the FIRST challenge you face when working with Spark. 

Once you've mastered solutions to that problem, the next level of trouble comes from external dependencies. Calls to APIs, Databases, and other networked resources are going to give you heartburn. They often aren't designed to handle 150+ open connections from a Spark cluster and will start to overload. 

So in those situations you have to first get Spark to go fast. . .and then figure out how to intelligently reign it in and slow it down. That isn't something [Spark wants to do]({{< ref "spark-jdbc-throttling.md" >}}). 

I have more to share on this problem, but that'll wait for another post.
