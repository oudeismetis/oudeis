+++
title = "Cognitive Load is the Mind Killer"
date = "2021-09-30"
categories = [ "thoughts" ]
+++

Your team can handle less complexity than you think
<!--more-->

I used to believe that wireframes were something that devs and designers could visualize in their minds, but clients could not. Sure the client would SAY they understood the design and how application components interact, but they weren't able to have their mind's eye follow button clicks like the dev team and designers could.

I now believe that devs and designers aren't good at this either.

### The human brain can only take so much

I used to build optical illusions for a haunted house in high school. 

We like to think our brain records everything we see, hear, etc. The truth is our brain takes sample frames, much like a film camera, and fills in the blanks with it's own assumptions. It's worse than that as our brain will even filter out things in those frames if it decides that thing is unimportant or not going to change. (think of the boring chair in the corner). A good example of this is growing evidence that humans [perceive less color in our periphery vision](https://www.sciencedaily.com/releases/2001/05/010508082759.htm), not because of our eyes but because of our brains.

Overwhelm the brain with an interesting story, background music, and a shiny object and you have the recipe for the perfect scare (or a magician's slight of hand)

When this happens the brain is under high [cognitive load](https://en.wikipedia.org/wiki/Cognitive_load).

### We see it all around us

Software developers talk about this topic a lot, but usually as it relates to how long it takes them to get back into the codebase in the morning. The time needed to fill their brain with all the context they need to know what the next code change should be.

It also comes up with software bugs in production and the amount of time it can take a developer to find the bug, but also determine a fix for it.

```
"Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it."
```
[Brian Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan)

But we also bring with us a base level of cognitive load from the common stresses in our life.

- Do I have enough money to pay that bill?
- Is my brother/boss/coworker mad at me?
- Didn't my spouse remind me to do something this morning?

And every project, by just existing, has cognitive load on all involved. Even if it hasn't started yet or is winding down, people are "thinking" about. So the more projects your team has, the higher their load.

![Team velocity drops as cognitive load goes up](/img/2021/cognitive_load.png)

Many projects themselves have so much cognitive load that all involved are constantly in firefighter mode. Not just devs but tech leads, PMs, clients, etc. If you don't take the time to pay off code/org debt then you are almost destined to be in a downward spiral of ever growing cognitive load as you continue to layer on features.

I believe that Google's findings that [psychological safety](https://rework.withgoogle.com/print/guides/5721312655835136/) is central to effective teams is in part due to the lower cognitive load on the team, allowing them to focus their energy more.

### Why can't things be simple?

Innovators who have a good idea are often afraid that the idea is too simple/small and not impressive enough or that someone will steal it. This often leads to making their idea more complex by adding a bunch of visionary features and...hey...lets throw in AI or Machine Learning for good measure!

- Complicated requirements cause a lot of cognitive load
- Cognitive load leads us to feel a lack of control over the complex system
- This lack of control leads to fear as we don't fully understand all the moving pieces
- To gain back control, the first tool we reach for is often "making a plan"
- Plans make us feel good. Having a nice linear path to follow gives us a warm fuzzy
- But plans add more cognitive load as all involved try to stick to the plan
- More fear > more need to control
- So lets add wireframes! Spend a bunch of time drawing out what things will look like
- Gantt charts, pert charts, work breakdown structures...
- Lets keep going. If we hurry we can have the whole thing planned out in about 9 months
- We can then send it over to the engineering team to build it all. I'm sure our plan will survive contact with production

Our efforts to deal with our fear of complexity result in more complexity.

```
"Fear is the mind killer" -Dune
```

This default reaction we have to fear and cognitive load is why I think most Agile projects back slide into Waterfall.

### Elevator pitches matter...for yourself and your team

I believe there is a better way and it's centered around minimalism.

If you can't explain it simply you don't understand it well enough.

If the vision is simple the team doesn't have to think as hard to understand things. The less your team has to think the better.

Having big ideas still matters, but there is a time and place to revisit them and that isn't daily or weekly. It's more like a monthly chat to ensure what is being built still matches the vision.

For software developers, reducing abstractions and clever code in favor of more readable solutions will help. I've written before (2013) about [mitigating Code Complexity for Hard Problems]({{< ref "mitigating-code-complexity-for-hard-problems.md" >}}).

Same applies to project planning. The more moving pieces the more little details and edge cases your team will miss. You'll only catch them after you've built it and have it in your hands.

You cannot allow your big ideas and plans to over-complicate the implementation being built today. The sooner you can get the product in your hands the sooner everyone (client, devs, and customers) can have a shared understanding of the strengths and limitations of where you are.

From that solid foundation, iterate.

The cognitive load of fast iteration on specific features is usually very low.
