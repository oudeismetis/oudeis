+++
title = "The Cognitive Load of Bugs"
date = "2023-08-26"
categories = [ "thoughts" ]
image = "img/foo.jpeg"
showonlyimage = false
draft = true
+++

Recording and tracking bug fixes can waste your teams time
<!--more-->

I don't mean to say that fixing bugs is a waste of time, but I often see teams wasting too much time doing planning activities around them?

Have you ever added a bug to your backlog, only to realize later there was already a ticket/story for it?

Pulled on a bug task only to be unable to reproduce it?

Have a sea of backlog stories that you know in your heart no one will ever fix?

I've been on many teams where hours were wasted every month discussing and prioritizing long lists of bugs that were destined for the "always deprioritized" island of misfit toys.


## The squeaky wheel

## A lack of imagination

our inability to see bugs when we create them

## Is a bug a bug?

Wasting time on bugs and edge cases that users will never notice or care about


Keeping track of bugs. Can be a dangerous cognitive problem for both an engineering team and a product team. You know, as a dev is going through the code or as a dev is implementing a feature, a constantly thinking of 20 30 Different little corner cases in edge cases. That they might be able to solve right then and there The problem is each one of those corner and edge cases.
I mean first off, we don't know what How the users are going to respond how the product team is going to respond. So if i sit there and i code out those 20 different edge cases that's going to take a lot of extra time and effort. And in the end i'm going to find out that the feature is going to change requirements going to differ.
And you know, half of those corner cases that i fixed aren't going to be relevant anymore. Also, each one of those corner cases is probably a line or two of code and that adds up quick. Which even if they are a good corner cases, that could be fixed. You're now talking about a lot of extra code that's going to have to get maintained over time code that's going to distract devs in the future.
So when i'm trying to debug some other problem and i go into that file now you've got a lot more extra lines of code that i have to read through before i figure out that those lines of code aren't relevant to the problem. I'm trying to solve and that i can safely ignore them.
And in the end of the day, Was fixing those corner cases, impactful for the user or where they just kind of annoyances that only the product team would notice or only engineers would notice And so oftentimes as engineer. It's beneficial to ignore the edge cases, and just focus on the most important critical path for that feature.
And if something's truly important, it's going to come back as a bug, it's going to come back as a high priority bug. Now, to flip on that conversation, let's talk about bugs them. So, on the product team, on the product side, you're going to constantly be noticing tons of bugs in the app.
The app will always have bugs and i've watched teams get into this trap where they start tracking every single bug, or they try to to store an update every single bug in the bug tracking system. And they end up with this massive, huge backlog of things. And the thing is as a developer, as i'm coding, oftentimes, i'll be implementing a new feature and i'll come across a bug, but i'll think it's a bug.
I just introduced as part of that feature. And so i'll just fix it. Not realizing that it was a bug that got reported six weeks ago and is sitting somewhere in the backlog. So not only will i fix that bug. Just organically in my work. But i won't know that there's something in the backlog that can be marked as done.
I won't know to tell somebody to go retest a thing. And so i've seen projects in the past where You know, the backlog. It's so full of things that especially bugs that at some point, you know, the CEO or somebody will say, Hey, no. We need to take like two weeks and do nothing but bug fixing just go through and kill all these.
And the dev team goes and does that. And what do they find? Half of the bugs. Can't be reproduced. And they get marked as what we call obe overcome by events because somewhere in the course of changing other code, those bugs disappeared. And so now there is all this effort in bug hunting, there was all this effort and documenting those bugs.
All this effort that when it's talking about them as a team, probably discussing them maybe showing in demoing. Here's the bug that i'm seeing All this time, just having meetings and discussing about all these tiny, little things that don't really matter to the core product and then engineering taking their time to go, try to reproduce those bugs and fixing them, only to find out that they got fixed.
Anyway, it's all one big, massive distraction. Both on the product side and the engineering side. That doesn't really drive. Efficient delivery of Progress to users. And so, in my mind, The best way to solve this is for the most part engineers. Shouldn't worry about educases, right? You should always be building for the happy path of the current thing you're building.
What is the mvp for this feature? What is the, you know, mvp for that mvp, right? Get the most minimal viable thing out there and deliver to products so that they can test it and see, hey is as good enough to go into production. Or are there some critical bugs and edge cases and nice to have that need to be there before we can launch it.
And then, even then products should only ever be thinking about what are the top three things. So what are the, you know for a given feature? What are the you know if it's not quite ready to go to production? What are the three things that's missing? You know, at most could be one thing but at most three things only what are those three things missing.
Go do those things and then let's discuss again. If it's ready to launch. And then even when it is launched in production and we know there's bugs and there's corner cases and all these other things going on. And producted, another testers, and other people are in production testing. The conversation should only ever be about what are the top three bugs in production today?
And those are the only ones that should be prioritized. There's the only ones that should be in the backlog. For dev to work on. And when one of those gets fixed, well, then let's talk about the next one on that list of That should be moved up to that list of top three bugs.
And as long as you keep operating in that mindset, what you'll find is, a lot of those smaller bugs that you would have normally just thrown in the backlog and never prioritize. Those will all get magically fixed along the way or we'll just, you know, there'll always be something more important than them.
The team will have tighter focus. They'll be less cognitive load because it'll be less things that we're talking about. So less cognitive load. And everything will run much more efficiently. And we won't be carrying this burden of all these things in the backlog. That feel like they matter when they really don't and all they do is distract us.
