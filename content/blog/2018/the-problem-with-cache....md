+++
title = "The problem with cache..."
date = "2018-07-19"
categories = [ "thoughts" ]
weight = 1
draft = true
blogimport = true 
+++

Problems:<br />- Can make it hard to debug code if you cache locally during dev or are debugging a higher environment.<br />- Can cause tests to fail if tests aren't using a dummy cache. (or hide bugs where something is cached that shouldn't be, so the state has changed, but a user sees the old version) <br />- Can hide performance issues that affect the underlying logic<br />- Sooner or later, some user is going to cache miss and be faced with an sins committed there<br /><br />Core principles:<br />- A call to the asset should work "normally" without cache. If you cache a page that calls a function that spikes memory or is incredibly slow, thats code smell.<br />- If you are worried about spike loads (Oprah tweeting a link to your site), set a cache for 10 seconds. You'll get a max of 6 calls per minute, which is more than enough for any server.<br />- If you have a page that never changes, cache it for a day. Only one user will trigger the call.<br />- If you have a high powered site that sees a million visitors a day, start caching for ~1year (static images, static pages, etc.)<br /><br />Cache is the most powerful when it's used as a tool for smoothing server request demands. Used to aggressively, you can find yourself with bugs that only a small percent of users see, that can't be reproduced, and you'll find yourself questioning reality.
