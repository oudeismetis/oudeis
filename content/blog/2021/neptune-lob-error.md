+++
title = "AWS Neptune LOB Support"
date = "2021-06-25"
categories = [ "thoughts" ]
tags = ["aws", "dms", "neptune", "lob"]
+++

Debugging errors with DMS migrations from Postgresql
<!--more-->

I had AWS' Data Migration Service (DMS) working for a single Postgresql table I was working with, but when I moved onto a 2nd 
table weird things would happen.

## What's an LOB?

Poking around in the CloudWatch logs I found the following:
```
Column 'foo' is unsupported in table def 'public.bar' since the LOB support is disabled
```

LOB? What's a LOB? Large Binary Objects? I don't have anything like that in my Postgres table?

Turns out one thing that was different about this new table was that several columns were using the **TEXT** type. Unlike 
**VARCHAR**, **TEXT** isn't bound to a specific length and can be used for storing paragraphs of information. As a result, DMS 
handles it as a **NCLOB** when ingesting the data.

So the issue was that the **TEXT** datatype is a **LOB**. 

Well, DMS has settings for [enabling LOB support](
https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.TargetMetadata.html).

But turning on LOB support was not working. I experimented with several of the setting combinations but nothing was working.

After a little more digging in the logs I found this message:
```
LOBs are not supported by target. LOB support is disabled
```
DMS supports a number of **sources** (Postgres) and **targets** (Neptune).

So it seems that LOBs aren't supported For DMS to Neptune. This wasn't documented anywhere, although I did come across a couple of
bits of documentation and stack overflow posts that hinted at this being a possibility. So no matter what LOB settings I tweak,
those setting are getting ignored.

Disappointing and it seems that DMS has a lot of little edge cases like this depending on what your sources and targets are.

## Wouldn't LOBs be bad in Neptune?
Probably. Large objects can especially be a problem if you are searching them as part of a query. In my case these DB columns
could have easily been short length **VARCHAR**s instead. Often the choice to use **TEXT** is made because the length of the data
isn't yet known and there is a fear that it will be longer than any length choice made. If you are facing a similar challenge to
this one you should measure the size of your data and decide if the solution below is a good one or if you should reconsider where
that data should live as part of your migration.

The work-around is to create a VIEW where the types are changed to something that isn't a LOB.
```
CREATE VIEW my_view AS 
  SELECT id, CAST(name AS VARCHAR(10)), CAST(email AS VARCHAR(60)) 
  FROM bar;
```

DMS does support ingesting a VIEW, but you need to set **table-type** in your Mapping Rules as part of your Database Migration Task.
```
{
  "rules": [
    {
      "rule-type": "selection",
      "rule-id": "1",
      "rule-name": "1",
      "object-locator": {
        "schema-name": "%",
        "table-name": "foo",
        "table-type": "all"
      },
      "rule-action": "include",
      "filters": []
    }
  ]
}
```

## Useful Links

* [AWS guide for loading Neptune via DMS](https://docs.aws.amazon.com/neptune/latest/userguide/dms-neptune.html)
* [Postgresql as DMS Source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html)
* [Neptune as DMS Target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html)
* [Troubleshooting DMS migration tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Troubleshooting.html)
* [StackOverflow for a related issue](https://stackoverflow.com/questions/57961882/aws-dms-database-migration-services-full-lob-not-working-for-sql-server)
