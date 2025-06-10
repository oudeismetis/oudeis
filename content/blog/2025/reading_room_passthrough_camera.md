+++
title = "Passthrough Camera API in Godot"
projectslug = 'vr-reading-room'
date = "2025-06-10"
categories = [ "projects" ]
image = "img/2025/reading-room/passthrough_works.gif"
showonlyimage = false
+++

Meta finally opened up the Camera API to devs  
I got it working in Godot
<!--more-->
---

After over a month of banging my head on the wall, I finally got the new Meta Passthrough Camera API working on Godot in VR.
:rocket:

The final function that works for initializing everything looks like this:

{{< highlight python "linenos=table,linenostart=34" >}}
func _initialize_passthrough_feed(granted: bool) -> void:
	print("Initializing Meta Quest PassThrough Camera API")
	CameraServer.monitoring_feeds = true
	var feeds: Array[CameraFeed] = CameraServer.feeds()
	if len(feeds) < 2:
		printerr("Not enough cameras found; Not getting passthrough images")
		return

	var camera_display: MeshInstance3D = get_node("Table/CameraDisplay")
	var camera_viewport: SubViewport = camera_display.get_node("CameraViewport")
	var texture_rect: TextureRect = camera_viewport.get_node("TextureRect")
	var material: StandardMaterial3D = StandardMaterial3D.new()
	var camera_texture: CameraTexture = CameraTexture.new()
	# Meta Quest Passthrough Camera settings
	var camera_choices: Array[Dictionary] = [
		{ "id": 0, "width": 320, "height": 240 },
		{ "id": 1, "width": 640, "height": 480 },
		{ "id": 2, "width": 800, "height": 600 },
		{ "id": 3, "width": 1280, "height": 960 }
	]
	var camera: Dictionary = camera_choices[3]

	# feeds[0]: avatar
	camera_feed = feeds[1]
	camera_feed.set_format(camera["id"], {"width": camera["width"], "height": camera["height"]})
	camera_feed.feed_is_active = true

	camera_viewport.size = Vector2(camera["width"], camera["height"])
	texture_rect.size = Vector2(camera["width"], camera["height"])
	texture_rect.texture = camera_texture
	camera_texture.camera_feed_id = camera_feed.get_id()
	material.albedo_texture = camera_viewport.get_texture()
	material.emission_texture = camera_viewport.get_texture()
	camera_display.material_override = material
{{< / highlight >}}

### All the little speed bumps I ran into:
- Does not work on the Meta Quest 2, so I had to bite the bullet and buy a Quest 3
- Godot didn't have support for cameras on Android, but just added it so I needed to grab a development build (Godot 4.5-dev4)
- An extra plugin to further improve the CameraServer [CameraServerExtension](https://github.com/j20001970/godot-cameraserver-extension)
    - Not sure why this is still needed at this point
- Had to first test on a 2D Godot project running on my phone to confirm the code and plugins are all set up right
- Spent a bunch of time digging into issues and solutions that had no effect
- Built out test code to load static images from files to confirm I could display them in the app to later validate that the feed works.
- Had to (?) version bump a bunch of dependencies to newer versions
    - godot-xr-tools v4.4.0
    - godot_openxr_vendors v4.0.0
    - godot-cameraserver-extension v2025.04.06
    - Android SDK Build Tools 35
    - Android NDK 27.2.12479018
- Couldn't test the cameras in the editor or on XR Simulator
- Pass a new custom permissions (**horizonos.permission.HEADSET_CAMERA**)
- Spend a bunch of time confirming permissions were being picked up correctly by the headset
- Dealt with race conditions were small waits were needed before later steps could succeed
- Sacrificed a goat
- Took the headset on and off my head 100+ times
- Set the camera feed format or it won't work
- Figure out how to turn the feed into a texture with a proper material or it won't work
- The first time the app loads the cameras won't work anyway for reasons (known bug)
- Have it magically work randomly after eliminating a dozen reasons why it wouldn't work


![Ghostbusters Chore Gif](/img/ghostbusters_chore.gif)

If you want to follow my progress more closely, I stream on Twitch and YouTube Monday&Wednesday (~10AM Eastern).  
I then post more organized devlog updates on my YouTube channel. (as well as here on my blog obviously)

### A more in-depth look into this work

{{< youtube id="_hqEwrW7qDk" >}}
