+++
title = "VR Reading Room"
slug = "vr-reading-room"
date = "2025-05-30"
tags = ['godot', 'vr']
image = "img/2025/reading-room/sky_change.gif"
showonlyimage = false
active = true
weight = 1
+++

A better way to read to maintain flow state or stay lost in the story
<!--more-->
---

### What is it

**Reading Room** is a VR app that adds to the ambiance of reading physical books in the real world.

It lets you take a physical book off of your book shelf, open it (with the headset
on), and then matches the scene around you to the content of what you are reading so you can get
lost in the story or stay in flow state for work.


### Current Capability

I have the core loop of the app running on a Meta Quest 3.

* Using the cameras on the headset, it takes a picture and runs OCR on.
* It then displays that text on a book you can hold in VR.
* It will switch the sky between day and night to match words it finds on the page.
* This will then be repeated as it takes another image from the page.

![Reading Room VR OCR Working](/img/2025/reading-room/devlog_0.gif)

### Screenshots

{{< figure
  src="/img/2025/reading-room/reading_room_tech_demo_1.png"
  alt="Go find a book and sit somewhere comfortable"
  width="100%"
  class="margin-0"
>}}

{{< figure
  src="/img/2025/reading-room/reading_room_tech_demo_2.png"
  alt="Processing"
  width="100%"
  class="margin-0"
>}}

{{< figure
  src="/img/2025/reading-room/reading_room_tech_demo_3.png"
  alt="Daytime environment"
  width="100%"
  class="margin-0"
>}}

{{< figure
  src="/img/2025/reading-room/reading_room_tech_demo_4.png"
  alt="Nighttime environment"
  width="100%"
  class="margin-0"
>}}

### Challenges

* Calling C++ code libraries from Godot GDScript has proven to be more work than I thought (mostly
  slow and tedious learning)
* OCR quality and speed
* Getting the passthrough camera to work in Godot was a HUGE challenge given how new the API was. I ran into enough issues that I
  put out a dedicated video on YouTube to help others. {{< youtube id="_hqEwrW7qDk" >}}

### Abandoned Ideas

**eBook reader**

I originally thought about making it a ebook reading. But that would require a LOT of extra code
and effort. This is also an idea I've seen others have. I expect there will be real competition for that style of app.
Eventually Kindle and other existing companies will offer their apps in VR. Instead of competing
with them, I decided it's better to think of a bigger/grander idea.

**immersive world**

I briefly toyed with the idea of bringing in tons of detail so you really feel like you are in a castle while reading a page that
takes place in one. I may implement some form of this eventually, but for now I think the spirit of the app is that it doesn't
distract you or substitute your imagination. If it's doing it's job well, you forget that you are in VR and are lost in the story
and your own head.

**AI Generation**

I'll never count this one out, but for the moment I want to try and avoid using this if I can. The VR headsets only have so many
resources and I don't know how demanding it will be to have the cameras on, running OCR all the time, and possibly needing
something like openCV to help with pre-processing. On top of that, I want to avoid calls to the internet and maintaining servers
or live services. If the network goes down, the app should still work. Also, AI is still very new and changing rapidly. So for all
of these reasons, I'm holding off. But as the project matures I will likely give this another look to see where it would be
appropriate to use it.

### Original Inspiration

I've been workshopping this idea since 2020.

Reading books with a small child around can make it difficult to get your imagination lost in a book. I would listen to classical
music with earbuds which would help a lot, but thought about how to take things further.

I remembered some of the mixed reality R&D I did years before and so the idea of using VR/AR to aid ones imagination while 
reading excited me. I did a bit of googling and quickly found others who built similar VR/AR experiences (so I wasn't crazy). 

But none of them had implemented my crazier ideas, probably because VR headsets were just now adding the tools needed to make 
them a reality. I had been wanting to create a compelling VR experience for a while and this felt like the right idea with the 
right timing.

### Inspiring Research (2020/2021)
* https://m.slashdot.org/story/359258
* [Where to find books in the public domain](https://www.vice.com/en/article/kz4e3e/millions-of-books-are-secretly-in-the-public-domain-you-can-download-them-free)
* https://www.hathitrust.org/#
* https://duckduckgo.com/?q=book+reading+games&t=fpas&ia=web
* https://www.theverge.com/2021/4/27/22395923/sidequest-android-app-sideload-oculus-quest-2-virtual-reality-apps-games-experiences
* https://www.publishersweekly.com/pw/by-topic/industry-news/comics/article/84154-virtual-reality-check.html
* https://supermedium.com/
* https://immersionvr-reader.com/
* https://www.oculus.com/experiences/go/1397503436990351/
* https://www.chimerareader.com/
* https://bookriot.com/reading-in-virtual-reality-the-good-and-not-so-good/
* https://ilmk.wordpress.com/2017/05/24/now-you-can-read-your-kindle-books-in-virtual-reality/
* https://bookriot.com/what-are-the-possibilities-for-books-and-vr/
* https://www.reddit.com/r/OculusQuest/comments/cfz0a5/app_to_read_books_in_vr/
* https://www.oculus.com/experiences/go/2503371199677065/
* https://github.com/incshaun/VRCoolReader
