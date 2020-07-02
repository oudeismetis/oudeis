+++
title = "Spark Dict Update Df"
date = "2019-02-28"
showonlyimage = false
draft = true
+++

"Start with why"
<!--more-->

{{< highlight python "linenos=table" >}}
def update_from_dict(my_dict):
    def in_dict(col, my_dict):
        return my_dict(col, 0)
    return udf(lambda l: in_dict(l, my_dict))

# this is slow
elements = [i[elem] from i in df.select(col_name).distinct().collect()]
results = call_api(elements)
df = df.withColumn(col_name, update_from_dict(results)(col(col_name)))
{{< / highlight >}}
