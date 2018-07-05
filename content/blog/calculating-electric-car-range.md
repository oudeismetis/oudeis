+++
title = "Calculating electric car range"
date = 2012-12-01T08:36:00Z
updated = 2012-12-01T08:36:41Z
draft = true
blogimport = true 
[author]
	name = "Edward Romano"
	uri = "https://plus.google.com/118036157148722337915"
+++

Wolfram Alpha app where you plug in some variables. (where you live, where you work, etc.) It then tells you what you need to consider when buying an electric car. Perhaps what questions to ask the dealer. "How does the battery fair in cold weather?"<br /><br />App inputs:<br />Distance you normally travel on an average day: (commute plus maybe a quick errand)<br />Zip code:<br />number of cars in household:<br />Most you're willing to spend on a car: 20K, 25K, 30K, etc.<br /><br />App internal math:<br />use Zip code to find coldest,&nbsp;hottest&nbsp;and average temp.<br />Figure out a formula for both Tesla and Leaf to factor in the impact of weather.<br />Now have two numbers: Lower limit range for Tesla and lower limit range for Leaf.<br />If daily commute is less than both, we're good.<br />If daily commute is ONLY less than Tesla, check to make sure they picked at least $50K option.<br />If daily commute is more than both, throw a flag.<br />If number of household cars is 1, throw a flag.<br />If willingness to spend is less than Leaf, throw a flag.<br /><br />App output:<br />No flags - YES<br />1-2 flags - MAYBE<br />3+ flags - NO<br />For each flag they get, list why they got the flag.<br /><br />Paragraph content of document:<br /><br />Have a table showing a picture of the two cars, price, range, etc.<br />Explain some of the calculation above. Dispell some myths about electric cars. Cost savings of charging at home and less maintenence. Warn about the battery replacement fee. Talk about road trips.<br /><br />http://www.cbc.ca/news/canada/manitoba/story/2012/02/14/mb-electric-car-winter-cold-weather.html<br />google "electric car efficiency in winter"<br /><br />
