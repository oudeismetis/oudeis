+++
title = "missed-moment"
slug = "missed-moment"
date = "2016-09-15"
tags = ['python', 'Raspberry Pi', 'IoT']
image = "img/projects/missed-moment-v1.jpeg"
active = false
weight = 1
+++

The main functionality works. I've had a raspberry Pi running it almost constantly for 2 years now 
with rarely any issues.  

<!--more-->

#### What is it
A "privacy by design" IoT camera designed to capture all the precious moments in life. For when you 
wish you had just caught something on camera.  
Detailed setup instructions can be found on [github](https://github.com/oudeismetis/missed-moment)

#### Current Capability
- Immediately starts recording when powered on
- Upon button press, the last ~1 min of video is written to temporary storage
- Plug a USB device in. Any saved videos will automatically be written and the USB device ejected.
- As nothing is written until button press, video kept in memory is lost after a few minutes

#### Challenges
Audio support has been the biggest rabbit hole. There are ways to create a circular buffer of 
audio, but syncing the audio and video is difficult. This is a work in progress.

#### Abandoned Ideas
Dropbox and Slack support have both been added and work, but are unofficially supported.  
The reason being:  
- Mo features, mo bugs  
- One of the main goals of this project is to be "privacy first". So being able to work fully 
without access to the internet is important for this ~internet~ of thing.

#### Inspiration
I had a dropcam for a while and realized that there was no local viewing of the stream. Anything it 
recorded HAD to be sent to the dropcam servers. To view the live stream on your phone meant 
streaming that same (now highly delayed) feed from their servers. Insane, Insecure, etc. etc.

In addition, there were so many times when something funny would happen when I was out of the room 
(cats and newborn). Never seemed like I could get to the feed in time, even with the network lag.

So I build missed-moment.

#### Research
[Raspberry Pi Init Script](https://blog.lanyonm.org/articles/2015/01/11/raspberry-pi-init-script-python.html)

[Python SSDP](https://gist.github.com/dankrause/6000248)

[Another Python SSDP](https://gist.github.com/provegard/1435555)

[Recording Raspberry Pi Video](http://raspi.tv/2013/how-to-shoot-video-and-convert-it-to-something-you-can-edit-in-pinnacle-and-other-programs)

[More RPi Video Recording](https://www.raspberrypi-spy.co.uk/2013/05/capturing-hd-video-with-the-pi-camera-module/)

[Converting RPi Video Formats](http://raspi.tv/2013/another-way-to-convert-raspberry-pi-camera-h264-output-to-mp4)

[Working with USB in RPi](https://www.raspberrypi-spy.co.uk/2014/05/how-to-mount-a-usb-flash-disk-on-the-raspberry-pi/)

[Ejecting USB Devices](https://raspberrypi.stackexchange.com/questions/14843/how-to-eject-usb-device-on-raspberry-pi-not-just-unmount)

[Audio and Video in RPi](https://www.element14.com/community/thread/49732/l/high-quality-hd-audio-and-video-recorder-using-the-raspberry-pi?displayFullThread=true)
