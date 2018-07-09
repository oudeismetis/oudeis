+++
title = "Complimenting Code w/ Commenting"
date = 2013-02-16T12:00:00Z
updated = 2013-02-16T12:00:40Z
tags = ["smart match", "debugging", "code complexity"]
blogimport = true 
[author]
	name = "Edward Romano"
	uri = "https://plus.google.com/118036157148722337915"
+++

A few days ago I posted about <a href="http://oudeismetis.blogspot.com/2013/01/mitigating-code-complexity-for-hard.html">mitigating complex code</a> issues and introduced my opinion that commenting should be viewed as a last resort.<br /><br />That post kicked up some discussion on Facebook with some of my friends:<br /><br /><span style="background-color: #f1f2f6; color: #333333; font-family: 'lucida grande', tahoma, verdana, arial, sans-serif; font-size: 11px; line-height: 14px;">"Documentation and commenting is still important"</span><br /><span style="background-color: #f1f2f6; color: #333333; font-family: 'lucida grande', tahoma, verdana, arial, sans-serif; font-size: 11px; line-height: 14px;">-Close friend from college</span><br /><span style="background-color: #f1f2f6; color: #333333; font-family: 'lucida grande', tahoma, verdana, arial, sans-serif; font-size: 11px; line-height: 14px;"><br /></span><span style="background-color: #f1f2f6; color: #333333; font-family: 'lucida grande', tahoma, verdana, arial, sans-serif; font-size: 11px; line-height: 14px;">"I think it can be important, but I would much rather see time invested in writing better code and hiring more talented developers."</span><br /><span style="background-color: #f1f2f6; color: #333333; font-family: 'lucida grande', tahoma, verdana, arial, sans-serif; font-size: 11px; line-height: 14px;">-Former co-worker in response to above comment</span><br /><br />Of course I never meant to imply that code commenting isn't important. But I do believe that efforts should first be made to improve code quality, and then use commenting to compliment code that is either too complex or&nbsp;sophisticated&nbsp;to clean up.<br /><br /><b><u>So what does documentation/commenting mean to me?</u></b><br /><br /><u>Documentation does NOT mean </u>a single line telling the developer what this line does. That might be necessary for larger methods with many lines of code, but for a short and/or complex group of code such as this, you need to document&nbsp;<b>HOW</b>&nbsp;this line works.<br /><br />Below is a comment I consider good for the code in <a href="http://oudeismetis.blogspot.com/2013/01/mitigating-code-complexity-for-hard.html">my previous post</a>:<br /><br /><pre class="brush:perl" name="code" width="100%"># Perl.pl excerpt<br />#<br />#<br /><br /># Use smart match operator to compare values in hash to Regex<br /># Grep to capture all keys from successful smart matches.<br />my @matches = grep {$$hash{$_} ~~ /($target)/} keys %$hash;<br /><br /></pre><br />Note in the first line I make an explicit reference to "smart match". This gives the more junior developer something to google if they've never seen the ~~ operator before.<br /><br />Next, I reference the smart matching subcomponent in the wrapping functionality, which is a somewhat basic grep search.<br /><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody><tr><td style="text-align: center;"><a href="http://geekandpoke.typepad.com/.a/6a00d8341d3df553ef015432bf9167970c-800wi" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="400" src="http://geekandpoke.typepad.com/.a/6a00d8341d3df553ef015432bf9167970c-800wi" width="281" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;"><a href="http://scottdensmore.typepad.com/blog/2011/06/code-commenting-made-easy.html">source</a></td></tr></tbody></table><u>Documentation also does NOT mean</u> writing a book. If you find yourself writing 10 lines of code comments to explain something, you'll often find that in addition to no one actually reading the comments, you probably don't truly understand the code yourself. Unless your goal is purely job security, it's your duty as a good engineer to leverage the <a href="http://en.wikipedia.org/wiki/KISS_principle">KISS Principle</a>&nbsp;(Keep It Simple, Stupid) and make life easier for other engineers.<br />Besides, it's also a way to double check yourself. As Einstein once said:<br /><i>&nbsp; &nbsp; &nbsp;"If you can't explain it simply, you don't understand it well enough."</i><br /><br />All too often I see developers implement code that "works" without a&nbsp;truly&nbsp;deep understanding of what they actually did and the&nbsp;implications&nbsp;of it. That's a recipe for bugs and side effects.<br /><br />You also don't want to handhold the&nbsp;more junior&nbsp;developer here either. There are some things you just have to assume they are smart enough to understand. (Like the hash reference %$ in the code above)<br /><br />It's really:<br /><b><br /></b><b>When you combine common components (grep, regex, hash reference, smart match) into complex functionality that is not often seen in your code base or other projects, you need to comment.</b><br /><br />Often, I'll bet that if you follow some of this philosophy, your future self will thank you as he/she will likely be the first one to have to fix some confusing code you left behind.<br /><div><br /></div>