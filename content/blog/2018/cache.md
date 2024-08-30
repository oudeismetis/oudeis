+++
title = "Caching server requests without hurting yourself"
date = "2018-08-02"
categories = [ "thoughts" ]
showonlyimage = false
+++


Aggressively caching server requests, a great way to sweep bugs under the rug
<!--more-->

So you made something great – be it a photograph, blog post, or even just a forum comment –  and you put it on a website. Your website, to be specific. A small but consistent flow of traffic came in, until one day someone shared a link to your website from a little place called Reddit, and the flood gates opened. 

It’s the moment you’ve been waiting for – fame, virality, influencer status! . . .that is, until your servers start to melt.

Obviously no one wants this to happen. For those thinking ahead, questions of performance and scalability come into the conversation early. Depending on what you’ve built, there can be a number of problems to solve and optimizations to make. 

With optimization comes newer, unexpected problems. Caching in particular can be confusing. (What is caching?) But there are many types of caching, so lets visit one of them – server request caching.

**Why cache server requests?**

Important user requests have to be handled by the server. When a user attempts to register, log in and finally take those important actions we’ve been waiting for (buying something, creating content, submitting feedback etc.), the server must respond. 

But the rest of the time the user is clicking around, reading, and simply exploring your website. Those requests aren’t complicated, don’t require a database, and can slow our servers down, keeping them from serving the users taking important actions.

One of the most common solutions is to cache requests for images, css, html, and other static content using a CDN. ([What is a CDN?](https://en.wikipedia.org/wiki/Content_delivery_network))

If you have a static content only site like my personal site, you put the whole thing on a CDN and have virtually zero requests hitting the server. With a CDN, you can even host a scalable website on a tiny [Raspberry Pi](https://blog.cloudflare.com/dyi-web-server-raspberry-pi-cloudflare/) (though mine is on Amazon S3 with [Cloudfront](https://aws.amazon.com/cloudfront/)).

**Common Problems**

Cache is a great thing and seems like a no brainer, but it can also be an addictive drug that can be overused or misapplied. Viewing the cached version of something means you might not be seeing the most updated version or feeling the full performance implications of that asset.

**During local development** you may introduce bugs that you miss in local testing, but appear when your code moves into a higher environment where cache is cleared on deployment. Even if you think of this case, you still might go down a rabbit hole coding something for hours, only to realize that the page you were sanity-checking has been broken for hours. So you get in the habit of blowing away cache for every code change, but that can take time and is now integrated into your workflow. 

**On your test server**, some tests may fail because something small is cached and your test setup doesn’t clear that out (even though it wouldn’t be a problem in production). On the other hand, a test may pass because everything works great without caching, but in production that page/component/asset is cached, causing bugs for users.

**On that slow page in production**, a performance issue in compute logic might not be visible because the results are loading from cache. But sooner or later, some user is going to cache miss and be faced with any sins committed there. This can result in seemingly random memory and response spikes that affect individual users and are difficult to reproduce.

**Avoid Code Smell**

A call to a page/component/asset should work "normally" without cache. If you cache a page that calls a function that spikes memory or is incredibly slow, that is code smell. Create pages that are performant and stable without cache. A cache miss on that page should be an annoyance, not a problem.

It's common to feel the desire to just cache everything for ever, but as demonstrated above, this can cause problems.

Cache is also not a hammer – there are different ways to apply it for each situation…

**Common Situations and Strategies**

**Spike Traffic:** Oprah tweets a link to your home page and traffic goes from zero to one million in a minute. The fix is simple: set a cache on that page for ten seconds. You'll get a max of six calls per minute, which is more than enough for any server.

**Static Content That Never Changes:** This may include your logo, about page information, footer information, etc. Cache them for a day. One user will trigger the call and may perceive a wait for moment or two, everyone else will get a much faster experience.

**The Edge Case:** You have a high powered site that sees a million visitors a day: Everyone else has been caching everything for ~1 year, but your site is one of the FEW that should actually be doing that. You want to avoid as many calls to your server as possible, so just about everything should have a cache header for the user’s browser and should be held by your CDN for as long as possible. This means your deployments are more complicated, but if you are in this category you probably already know this.

**Conclusion:**

Cache is the most powerful when it's used as a tool for smoothing server request demands. Used too aggressively, you’ll find yourself with bugs that only a small percent of users see, that can't be reproduced, and will have you questioning reality.

