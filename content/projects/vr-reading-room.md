+++
title = "VR Reading Room"
slug = "vr-reading-room"
date = "2025-03-05"
tags = ['godot', 'vr']
image = "img/2021/reading-room/godot_vr_cube.gif"
showonlyimage = false
active = true
weight = 1
+++

A better way to read to maintain flow state or stay lost in the story
<!--more-->
---

### What is it

**Reading Room** is a VR app that lets you take a physical book off of your book shelf, open it (with the headset
on), and will match the ambiance around you to the content of what you are reading so you can get
lost in the story or stay in flow state for work.


### Current Capability

You can load the experience into Google Cardboard on android and toggle the color of a cube if you look and click on it.
(Baby steps!)
![Godot VR first steps](/img/2021/reading-room/godot_vr_cube.gif)

### Challenges

- Calling C++ code libraries from Godot GDScript has proven to be more work than I thought (mostly
  slow and tedious learning)
- Meta and Google have both announced their intentions to open up API access to the passthrough
  cameras in early 2025, but that has not happened yet

### Abandoned Ideas

**eBook reader**

I originally thought about making it a ebook reading. But that would require a LOT of extra code
and effort. This is also an idea I've seen others have. I expect there will be real competition for that style of app.
Eventually Kindle and other existing companies will offer their apps in VR. Instead of competing
with them, I decided it's better to think of a bigger/grander idea.


### Inspiration

I've been workshopping this idea since 2020.

Reading books with a small child around can make it difficult to get your imagination lost in a book. I would listen to classical
music with earbuds which would help a lot, but thought about how to take things further.

I remembered some of the mixed reality R&D I did years before and so the idea of using VR/AR to aid ones imagination while 
reading excited me. I did a bit of googling and quickly found others who built similar VR/AR experiences (so I wasn't crazy). 

But none of them had implemented my crazier ideas, probably because VR headsets were just now adding the tools needed to make 
them a reality. I had been wanting to create a compelling VR experience for a while and this felt like the right idea at the 
right timing.

### Research
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
