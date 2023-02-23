+++
title = "Running Cypress Github Action after Heroku deployment"
date = "2023-02-23"
categories = [ "thoughts" ]
showonlyimage = false
+++

The best way to test your Review Apps
<!--more-->

---

Running unit tests and linters automatically every time a dev pushes a commit to a PR is amazing.

You really don't want to wait until your code is "done" to find out if there are issues with it and running these things manually all the time isn't fun.

Further automating your CI/CD with Heroku or other platforms helps even more. Configuring [Review Apps](https://devcenter.heroku.com/articles/github-integration-review-apps) means that, in addition to unit tests and linters, you'll also have a live app you can test that closely resembles production. Say goodbye to the "well it [worked on my machine](https://blog.codinghorror.com/the-works-on-my-machine-certification-program/)" excuse when something breaks in staging.

The final piece to this puzzle is often running end-to-end tests against that live Review App.

But for me there was a small nagging problem here. [Github Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions) are often setup to run on push. So my [Cypress tests](https://www.cypress.io/) would run at the same time as my other tests (immediately).

As many devs know, it's often that "one final small tweak" you push that can break everything. Given that Heroku can take several minutes to build and deploy, this means that your Cypress tests are likely testing your LAST commit, and not your current one.

## The quick hack solution

The first quick thing I did was add an explicit sleep for 5 minutes. This worked, but of course wastes time and money and who knows if the app is even ready then. Should the build fail you wouldn't know and will just be testing an older commit by accident.

## The hard solution

When I first took on this problem, it seemed to be harder than I initially thought. There seemed to be no way to know when Heroku was finished and I found [several articles](https://niteo.co/blog/staging-like-its-2020) online of others figuring out their own [work arounds](https://www.enekoalonso.com/articles/issue-7).

In the end I built my own complicated solution that involved Heroku making an API call to Github at the end of the release phase. You can [view the code](https://github.com/thinknimble/tn-spa-bootstrapper/pull/99) and see all the details on one of the implementations of it, but I won't detail it here as I found a MUCH better solution.

## A simpler way

Turns out that Heroku was already making an API call to Github every time it finished a release. I [couldn't find it documented anywhere](https://devcenter.heroku.com/articles/github-integration) and discovered it after having an "I wonder" moment while digging through Github's vast API docs.

Heroku creates a [Deployment Status](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#deployment_status) for the commit when the release finishes. This status is connected to the individual commit (so it won't accidentally trigger a newer Github Action should you quickly push two commits back-to-back)

That status also includes an [Environment URL](https://docs.github.com/en/rest/deployments/statuses?apiVersion=2022-11-28#create-a-deployment-status), so you don't have to guess or compute the URL that you need to test.

Your code can thus be [simplified](https://github.com/thinknimble/tn-spa-bootstrapper/pull/150) to look like this:

{{< highlight python "linenos=table" >}}
name: Cypress Tests
on: [deployment_status]

jobs:
  Firefox:
    if: github.event.deployment_status.state == 'success'
    runs-on: ubuntu-latest
    container:
      image: cypress/browsers:node16.14.2-slim-chrome103-ff102
      options: --user 1001
    steps:
      - uses: actions/checkout@v3
      - name: Run against ${{ github.event.deployment_status.environment_url }}
        uses: cypress-io/github-action@v4
        with:
          working-directory: client
          browser: firefox
        env: 
          NPM_CONFIG_PRODUCTION: false
          CYPRESS_TEST_USER_EMAIL: "cypress@example.com"
          CYPRESS_TEST_USER_PASS: ${{ secrets.CYPRESS_TEST_USER_PASS }}
          CYPRESS_baseUrl: ${{ github.event.deployment_status.environment_url }}
{{< / highlight >}}

And that is literally it.

Cypress will now have a yellow status on your PRs until Heroku successfully finishes it's release.

## Lingering issues

There is a [known issue](https://github.com/actions/cache/issues/319) where `actions/cache` doesn't work with `deployment_status` events.

Also, if you push two commits quickly close together it'll run Cypress for both (wasting time and money) and there is a chance the Cypress run for the older commit would be testing a newer version of the app. (Rare and too small of an edge case to probably worry about)
