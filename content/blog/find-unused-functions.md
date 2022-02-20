+++
title = "Find Unused Functions"
projectslug = 'foo'
date = "2021-07-09"
categories = [ "thoughts" ]
image = "img/foo.jpeg"
showonlyimage = false
draft = true
+++

"Start with why"
<!--more-->

# TODO - Just put this in your .dotfiles instead

{{< highlight shell "linenos=table" >}}
#! /bin/bash

functions=$(find . -name "*.py" -print0 | xargs -0 grep "def " | sed 's/.*def //' | sed 's/(.*//')

for f in $functions
do
  if [[ $f != test_* ]]; then
    count=$(grep -r --exclude-dir=test $f . | grep -v "def " | grep -v ".pyc" | grep -c $f)
    if [[ $count == 0 ]]; then
      echo $f
    fi
  fi
done

{{< / highlight >}}
