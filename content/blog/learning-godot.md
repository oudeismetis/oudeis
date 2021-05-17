+++
title = "Learning Godot"
projectslug = 'vr-reading-room'
date = "2021-05-17"
categories = [ "projects" ]
image = "img/2021/reading-room/godot_first_game.gif"
showonlyimage = false
+++

A new platform for some of my video game ideas
<!--more-->

I have done some R&D work with video game engines in the past, mostly with [Unity](https://unity.com/) and
[Unreal](https://www.unrealengine.com/en-US/) and started with the typical tutorials to get my feet wet. 

Here is game a made with a tutorial back in 2015:
![First Unity Game](/img/2021/reading-room/unity_first_game.gif)

The most interesting result of my work back then was installing a button in a room that would trigger events (over the internet) 
in an identical room inside a running game. (Unreal Engine project and code lost sadly. Hopefully if I ever find it I'll post to 
Github and share it)

So now it's 2021 and I have years of R&D ideas stewing in my brain.

# So why switch to Godot?

Well, I was never really an expert at Unreal or Unity to begin with so I took the opportunity to re-evaluate the best tools to use
when doing gamedev in 2021.
I have a couple of friends in the game industry who pointed me to [Godot](https://godotengine.org/) as the best engine for small team side projects.

* It's 100% free
    * Unity/Unreal start free but will eventually charge you money
* It's open source
    * More transparency around new features, easier to lift open the hood to see how things work, etc
* It has a Python-like scripting language
    * Unity/Unreal use C#/C++
* Seemed to be MUCH easier to learn and get moving quickly

# Time for another tutorial game

I of course started with a [tutorial to create a 2D game](https://youtu.be/WEt2JHEe-do):
![First Godot Game](/img/2021/reading-room/godot_first_game.gif)

I can definitely agree that Godot feels much more logical to work with. 

# Diving into my first real project

I find the best way to learn is often to build something meaningful and stumble along the way.

My first project is going to be [reading-room]({{< ref "vr-reading-room.md" >}}), a VR experience that will be VERY simple from
the 3D modeling and animation side of things and will serve as a foundation for me to possibly experiment with things like:

* NLP
* Foveated Rendering
* OCR
* Or wherever my interests take me

I started by bootstrapped the projects and setting up developer debugging on my Android phone.

I created a simple scene with a floor and a cube to confirm that I could see something in Google Cardboard.

I then worked on getting access to the single button click that Google Cardboard gives you and was able to change the color of the
cube if you are looking at it and click the button.

![Godot VR first steps](/img/2021/reading-room/godot_vr_cube.gif)

(Impressive I know)

It's just a start and until I decide to shell out $$$ for a VR headset I'll stick with mobile VR and my single button click to
prototype things for now.

# Lessons learned so far

Couple of lessons learned so far. (Most for myself so I can search and find these notes later)

### Developer Access on Android
To run on Android you need to do a bunch of things to get your phone setup as a developer and to generate creds. Best to just
google the current best way to do this in the future.

### Setting up keystore for Android within Godot:
Project > Export > Add... > Android

`Release:` [path_to_my.keystore]

`Release User:` The one you set when creating the keystore

`Release Password:` Same

`Unique Name:` Probably best to customize this like `org.my_org.$genname`

Then just close. No need to actually export at first. USB debugging to phone should pop up an Android icon in the upper right
corner of Godot when a phone is connect.

### Live updates of changes to Android
Debug > Deploy with Remote Debug

### Google Cardboard Button Press
Project > Project Settings... > Input Map

Add a new input with a unique name

Click the `+` next to it and set it as `Mouse Button` > `All Devices` and `Left Button`

Now you can add a `_input()` that listens for something like `Input.is_action_just_pressed("click")`
