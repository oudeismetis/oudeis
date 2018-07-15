+++
title = "Dynamic Video"
slug = "dynamic-video"
date = "2017-06-23"
tags = ['python', 'blender', 'heroku', '3d']
image = "img/projects/trump_myst_book.gif"
active = true
weight = 1
+++

July 2018 Update:  
This was a side project in 2017. I need to fix some bugs and am planning to flip it from private 
to open source soon. This is a semi-active project at this point.
<!--more-->

#### What is it
Render videos/animations with substitutable images/video/text automatically via a Python REST API 
with Blender as a Heroku hosted service.

#### Current Capability
API hosted on Heroku.  
Pre-load the application with Blender files and some configuration.  
POST to the /render/ API endpoint, passing links to dynamic images and/or text to replace.  
Rendering takes a while, so the above call returns a job ID so you can call back for status.  
GET on the /status/ endpoint with a job ID will tell you if the job is finished. If finished, it 
will give you a download URL for the completed render.

Sample output above. Note that it can do video inside of video.


![Water pipe Blender render][1]  
The one I used was another animation I made in Blender previously. Used it because I had it.  


#### Challenges
Performance. It takes a long time to render.

#### Abandoned Ideas
Render farm.

May revisit this idea in the future as it's the main way to lower render times. It just requires a 
fair amount of tooling to get that working on AWS with something like [Brenda](https://github.com/jamesyonan/brenda).

#### Inspiration
Started out experimenting with 3D modeling.  
That led to scripting the creation of objects in Blender with Python.  
Which led to substituting text and images in Blender files pre-render.  
Which then led to learning "corner pinning", a technique for mapping three dimensional planes to 
surfaces in a regular video file. ex: [@TrumpDraws](https://twitter.com/TrumpDraws)   
Which made me want to automate all of this out into an application that handles all of the 
substituting and rendering for you.

#### Research
TODO

[1]: /img/projects/blender_water_pipe.gif
