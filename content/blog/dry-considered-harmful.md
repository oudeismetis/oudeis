+++
title = "Dry Principle Considered Harmful"
projectslug = 'foo'
date = "2023-09-18"
categories = [ "thoughts" ]
image = "img/foo.jpeg"
showonlyimage = false
draft = true
+++

"Start with why"
TODO - This is good at first. . .but becomes a rabbit hole, and only for 1 small piece of DRY. Probably better to re-write as 3-5 high level concepts of why it's bad.
<!--more-->

In a recent post about agile development I made a casual reference to [DRY considered harmful]({{< ref "waterfall-instinct.md" >}}), an opinion I've had for a long time and recently saw some code that reignited my thoughts on the subject.

### DRY?

"Don't Repeat Yourself" is the [DRY Principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) in software development that most of us learn early in our careers and usually starts with taking duplicate chunks of code and throwing them into a function somewhere so we can write something once and reuse it over and over again.

It is a very good principle, but I find it is overused and often done too early in the dev process and taken too far when used.

### Lets talk cognitive load


### Architecture can become too cemented

Sometimes the architecture decisions we make in our code can become hard to change. This can happen in a lot of ways (multi-class inheritance, unit tests exercising the implementation instead of the resulting behaviour, etc.).

In the case of DRY, a change needed for one usecase might result in that abstraction needing to change. . .but only for that usecase and not for any of the others.

To illustrate this with an example, I recently code reviewed an abstraction that was doing something like this.

{{< highlight python "linenos=table" >}}
def log_metrics(start=None, end=None):
    # This toy example has bugs
    start_str = datetime.strftime(start, '%Y-%m-%d') if start else 'n/a'
    end_str = datetime.strftime(end, '%Y-%m-%d') if end else 'n/a'

    logger.info(f'start={start_str} end={end_str}')
{{< / highlight >}}

Not too bad. There were a LOT of different jobs logging metrics about their results and it made sense to pull that out to a shared function. (obviously **log_metrics()** doing a lot more than the toy example above)

While reviewing the code I noticed that the function was usually being called with **datetime()** objects (expected) but was sometimes given integers and strings.

After calling this out, the implemented fix looked like this:

{{< highlight python "linenos=table" >}}
def log_metrics(start=None, end=None):
    # This toy solution is too complex
    if start:
        if start != 'n/a':
            start = datetime.strftime(start, '%Y-%m-%d') if start else 'n/a'
    else:
        start = 'n/a'
    if end:
        if end != 'n/a':
            end = datetime.strftime(end, '%Y-%m-%d') if end else 'n/a'
    else:
        end = 'n/a'

    logger.info(f'start={start_str} end={end_str}')
{{< / highlight >}}

So yes, this does solve the problems I raised, but now we have a new problem. Yeaaa, branching logic, but even more fundamental then that, we've now taken what was supposed to be a generic abstraction and coded edge case handling into it.

We have now increased the cognitive load on all developers who are debugging something near where this function is called.

When chasing down an odd bug and you see the call to **log_metrics()** in the code, you might be pretty sure the problem isn't in there, but you'll remember that it's doing something complicated and so you'll be forced to double check that logic to be sure. The example here isn't too crazy, but abstractions like this have a habit of collecting edge cases and thus get more complicated over time.

The more complicated it gets the more test code you'll need to write and the greater the cognitive load on everyone involved. (And test code is code so now you have cognitive load there as well)

You created the abstraction to make maintaining the code easier, but now you are running the risk of undermining all of that.

### My brain is out of memory. . .

{{< highlight python "linenos=table" >}}
def log_metrics(start='n/a', end='n/a'):
    # This toy example isn't the better
    start = datetime.strftime(start, '%Y-%m-%d') if isinstance(start, datetime) else start
    end = datetime.strftime(end, '%Y-%m-%d') if isinstance(end, datetime) else end 

    logger.info(f'{start=} {end=}')
{{< / highlight >}}

This solution isn't perfect by any means, but it accomplishes a couple of things. 

### So copy/paste code everywhere?

Certainly not. 
