+++
title = "Hashes in JS"
date = 2012-12-06T19:56:00Z
updated = 2012-12-06T19:56:48Z
draft = true
blogimport = true 
[author]
	name = "Edward Romano"
	uri = "https://plus.google.com/118036157148722337915"
+++

<br /><div class="MsoNormal" style="background-color: white; color: #222222; font-family: arial, sans-serif; font-size: 13px;">Working with hashes/objects in JS<u></u><u></u></div><div class="MsoNormal" style="background-color: white; color: #222222; font-family: arial, sans-serif; font-size: 13px;">doing this is bad:<u></u><u></u></div><div class="MsoNormal" style="background-color: white; color: #222222; font-family: arial, sans-serif; font-size: 13px;"><br /></div><div class="MsoNormal" style="background-color: white; color: #222222; font-family: arial, sans-serif; font-size: 13px;">var initWeek = { 'Sun':0, 'Mon':0};<u></u><u></u></div><div class="MsoNormal" style="background-color: white; color: #222222; font-family: arial, sans-serif; font-size: 13px;">var result = [];<u></u><u></u></div><div class="MsoNormal" style="background-color: white; color: #222222; font-family: arial, sans-serif; font-size: 13px;"><br /></div><div class="MsoNormal" style="background-color: white; color: #222222; font-family: arial, sans-serif; font-size: 13px;">for (var value in something) {<u></u><u></u></div><div class="MsoNormal" style="background-color: white; color: #222222; font-family: arial, sans-serif; font-size: 13px;">&nbsp; //some stuff<u></u><u></u></div><div class="MsoNormal" style="background-color: white; color: #222222; font-family: arial, sans-serif; font-size: 13px;">&nbsp; if (!result[value]) result[value] = initweek;<u></u><u></u></div><div class="MsoNormal" style="background-color: white; color: #222222; font-family: arial, sans-serif; font-size: 13px;">}<u></u><u></u></div><div class="MsoNormal" style="background-color: white; color: #222222; font-family: arial, sans-serif; font-size: 13px;">For some reason, (pointer?), every instance in result will be linked. Change one, change them all.</div>
