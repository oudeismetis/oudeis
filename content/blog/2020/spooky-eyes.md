+++
title = "Spooky Halloween Eyes with Arduino"
date = "2020-10-31"
categories = [ "thoughts" ]
image = "img/2020/spooky_eyes/spooky_eyes.png"
tags = ["arduino", "halloween"]
showonlyimage = false
+++

Spooky eyes in the bushes for halloween
<!--more-->

Quick and simple arduino project. I'd like to take credit for the idea/code, but I stumbled upon it a while back on [hackaday](https://hackaday.com/2018/10/28/easy-blinking-led-eyes-for-halloween/) with the code found in the comments on [youtube](https://www.youtube.com/watch?v=nbWs9cv3cqM).

This post and [youtube video](https://youtu.be/zr2J5BXy4O0) are to help others who wish to do the same project.

The main thing I did here was to make everything in a reusable way. The Arduino, LEDs, and project boxes. Everything is designed to come apart so I can reuse the pieces for other projects.

I especially enjoyed spending the time to craft the LEDs so I could reuse them for other projects. This gave me a chance to practice some soldering and use some heat shrink tubes.

One thing this picture doesn't show is the resistors that I soldered close to the LEDs and covered in the shrink wrap. Also, each LED wire is a different length. I did this so that some of the eyes can be further away, but also so that for future projects I can grab an LED with the correct length and not be stuck with only long wires.

![Making reusable LEDs](/img/2020/spooky_eyes/headers_and_heat_wrap.jpeg)

I bought cheap plastic food containers and drilled holes in them so I'd have a waterproof project container.

The inside is just black craft paper with strips of wax paper over the eyes to defuse the light (and tape of course).
![Water proof boxes](/img/2020/spooky_eyes/boxes.jpeg)

Prototyping. . .

![Testing the project](/img/2020/spooky_eyes/testing.jpeg)

The plastic food containers came as a set with a bunch of small ones, but also a large container. I taped the Arduino and breadboard to the lid of the large container. All of the wires and power brick for the Arduino also went in this box so the only thing exposed to the elements was an extension cord.

![Packing things up](/img/2020/spooky_eyes/packaging.jpeg)

One thing not shown in any of these pictures is that I used some Christmas ornament hangers poking out of the holes to hand each box from a twig in the bush. I suggest using two hangers spread apart a little to help keep them stable.

{{< youtube id="zr2J5BXy4O0" >}}

And last but not least, below is the code.

{{< highlight arduino "linenos=table" >}}
long randomLED;
long randomDelay;
 
void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
      
  randomSeed(analogRead(A0)); 
}
 
void loop() {
  // returns a random number between 2 and 24 inclusive
  // determines which LED will be blinked
  // the upper number determines roughly how often any individual LED blinks
  randomLED = random(2,25);
  // random number between 150 and 349 inclusive which determines blink duration
  randomDelay = random(150,350);
  
  if(randomLED == 2) {
    randomDelay = 500; // this makes "LED 2" always blink for half a second
  }
    
  digitalWrite(randomLED, LOW); // turns a random LED off
  delay(randomDelay); // blink/off duration

  digitalWrite(randomLED, HIGH); // turns the LED back on after blinking
  delay(randomDelay); // adds some "on" time so it doesn't look weird
}
{{< / highlight >}}
