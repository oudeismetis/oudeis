+++
title = "Dynamic Skybox in Godot VR"
projectslug = 'vr-reading-room'
date = "2025-05-09"
categories = [ "projects" ]
image = "img/2025/reading-room/sky_change.gif"
showonlyimage = false
+++

I am building a VR app that matches the environment to what you are reading
<!--more-->
---

Just a quick update for the [VR Reading Room project]({{< ref "vr-reading-room.md" >}}).

I took a quick detour to get the scene looking a little bit better.

For this I used the [Terrain3D](https://tokisan.com/terrain3d/) and [Sky3D](https://tokisan.com/sky3d/) plugins created by the team at [Tokisan Games](https://tokisan.com/).

I will likely attempt to do some procedural generation with this app, so having highly configurable land and sky utilities should
help me to do that (as opposed to me building something basic myself as a placeholder).

This has the added benefit of allowing me to prototype that dynamic behavior. So I started with a simple function to detect night
and day words in the text, and then changing the time of day to match.


{{< highlight python "linenos=table,linenostart=101" >}}
func _process(delta: float) -> void:
	_update_time():
{{< / highlight >}}

We will constantly check to see if we are near the right time of day. If so, freeze the clock.

{{< highlight python "linenos=table,linenostart=158" >}}
func _update_time() -> void:
	if abs(sky.current_time - current_time) < 1:
		# Now at desired time. Slow down the movement of time
		sky.update_interval = 0.1
		sky.minutes_per_day = 15
{{< / highlight >}}

Separately, when we finish OCRing a page, we will tell the clock to speed up.

{{< highlight python "linenos=table,linenostart=164" >}}
func _update_time_of_day(keyword: String) -> void:
	print("Moving the sun...")
	if keyword in ["night", "darkness"]:
		current_time = TIME.MIDNIGHT
	else:
		current_time = TIME.NOON
	# Fast Forward the sky
	sky.update_interval = 0.016  # 60 FPS
	sky.minutes_per_day = 0.15  # 15 seconds for 24 hour transition
{{< / highlight >}}

and then some test code to prove it out...

{{< highlight python "linenos=table,linenostart=222" >}}
var page: OCRPage = page_1

	var num_lines: int = page.lines.size()
	var halfway_point: int = int(page.lines.size() / 2)
	var first_half: Array[OCRLine] = page.lines.slice(0, halfway_point)

	for line: OCRLine in first_half:
		for word: String in line.text.split(" "):
			var cleaned_word: String = _get_simple_text(word)
			if cleaned_word in time_of_day:
				_update_time_of_day(cleaned_word)
{{< / highlight >}}


![Sky changing Gif](/img/2025/reading-room/sky_change.gif)

### A more in-depth look into this work

{{< youtube id="z3eCG_uby9k" >}}
