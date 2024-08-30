+++
title = "APRS transmitter sending last known GPS"
projectslug = 'thanos'
date = "2018-07-24"
categories = [ "projects" ]
image = "img/2018/thanos_tracker_gps.jpeg"
+++

It's hard to direction find a transmitter that won't transmit
<!--more-->

One of the features of the [FlexTrack](https://github.com/oudeismetis/FlexTrack)(My Fork) library 
is that it will only transmit an APRS packet if it can see at least 4 satellites.

The problem is that you can't put a large antenna on a High Altitude Balloon (HAB). So at low
altitudes, it is unlikely to reach a repeater or IGate. You'll end up going to the last known
coordinates, but from there you might find yourself poking around the woods and hoping for a
visual.

Many HABs solve this by adding a secondary system that turns on a buzzer at low altitude. That may 
be a feature we want in the future, but a simpler solution for now is to alter the arduino code to 
remember the last known GPS, and transmit that. Even if the location has deviated greatly, having 
it continue to transmit means we'll be able to direction find the exact landing location after 
arriving in the area during the chase.

Changes to [aprs.ino](https://github.com/oudeismetis/FlexTrack/commit/08f517be125c638e79602a052384ece29c2b0f26#diff-757ecebbb9d6dacf110111ab6c7430cd)
{{< highlight go "linenos=table,linenostart=41" >}}
// Declare variables outside of core loop
float LastLat=0;
float LastLon=0;
...
{{< / highlight >}}

{{< highlight go "linenos=table,linenostart=73" >}}
// Update variables when we have good GPS reception
if (GPS.Satellites >= 4)
{
  LastLat = GPS.Latitude;
  LastLon = GPS.Longitude;
}

if ((millis() >= NextAPRS) && (LastLat != 0) && (LastLon != 0) && (_txlen == 0))
  // use the cached variables during payload creation
  ...
{{< / highlight >}}

In addition. . .

We've begun building the final payload. The tracker is mounted with an on/off switch and we've 
begun carving a window in the styrofoam cooler for the GoPro.
