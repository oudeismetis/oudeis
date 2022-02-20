+++
title = "Shell Script Exception Handling"
projectslug = 'foo'
date = "2021-04-23"
categories = [ "thoughts" ]
image = "img/foo.jpeg"
showonlyimage = false
draft = true
+++

"Start with why"
<!--more-->

Refer to xonsh shell
https://medium.com/capital-one-tech/bashing-the-bash-replacing-shell-scripts-with-python-d8d201bc0989
Do some of this for missed-moment and blog it here?
https://github.com/oudeismetis/missed-moment/pull/7/files
Two separate posts?
https://github.com/stan-dev/math/issues/937


{{< highlight bash "linenos=table" >}}
#!/usr/bin/env bash

# set -o pipefail
trap 'rc=$?; echo "ERROR at line ${LINENO} (rc: $rc)"; exit $rc' ERR
set -E

main() {
  result=$(/.../foo.sh)
  result2=$(/.../food.sh || true)
  echo "$result" >> /tmp/foo.sh.log
  echo "$result2" >> /tmp/foo.sh.log
}

exec 3>&1
if output=$(main "$@" 2>&1 >&3); then
  echo "Success!!" >> /tmp/foo.sh.log
else
  echo "Fail??" >> /tmp/foo.sh.log
fi
{{< / highlight >}}

{{< highlight bash "linenos=table" >}}
#!/usr/bin/env bash

echo "Hello World"

exit 0
{{< / highlight >}}

{{< highlight bash "linenos=table" >}}
#!/usr/bin/env bash

echo "Hello Universe"

exit 1
{{< / highlight >}}

{{< highlight bash "linenos=table" >}}


{{< / highlight >}}
