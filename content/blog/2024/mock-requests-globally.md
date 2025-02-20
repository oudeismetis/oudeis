+++
title = "Mock Requests Globally"
date = "2024-08-30"
categories = [ "thoughts" ]
tags = ["python", "pytest", "mock", "requests"]
+++

Unit tests should never(:exclamation:) call the internet
<!--more-->
---

I've written a lot of unit tests with Pytest over the years and I've been on several Python projects where unit tests accidentally end up calling the internet.

Sometimes it's harmless or just slows the test runner down a little, but sometimes it causes instability and can either run up a bill on a service you pay for or accidentally result in a denial of service (hopefully only on yourself).

Here is a quick way to add safeguards so that if a unit test DOES call the internet, it's intentional and something your team has decided it wants to happen.


**conftest.py**
{{< highlight python "linenos=table,linenostart=7" >}}
 
@pytest.fixture(autouse=True)
def mock_requests(request):
    """
    This fixture will trigger an error if you try to call the requests library.
    In the rare instance that you need to disable this fixture, add this decorator:
    @pytest.mark.use_requests
    """
    if "use_requests" not in request.keywords:
        exception = Exception("Do not call the internet from a unit test")
        with mock.patch("requests.get", side_effect=exception), mock.patch("requests.post", side_effect=exception):
            yield
    else:
        yield
 
{{< / highlight >}}

**pytest.ini**
{{< highlight python "linenos=table,linenostart=8" >}}
 
markers =
    use_requests: Allow a unit test to call the internet
{{< / highlight >}}


And here is an example of skipping this rule for a test

**tests.py**
{{< highlight python "linenos=table,linenostart=74" >}}
 
@pytest.mark.use_requests
@pytest.mark.django_db
def test_password_reset(caplog, test_user, client):
    # fake our API call to the view that generates an email for the user to reset their password
    rf = RequestFactory()
    post_request = rf.post("api/password/reset/", {"email": test_user.email})
    request_reset_link(post_request)

    # Grab from the logs the actual URL link we would send to the user
    password_reset_creds = caplog.text.split("password/reset/confirm/")[1].split('"')[0]
    password_reset_url = f"/api/password/reset/confirm/{password_reset_creds}/"

    # Verify the link works for resetting the password
    response = client.post(password_reset_url, data={"password": "new_password"}, format="json")
    assert response.status_code == 200 
 
{{< / highlight >}}

Wait?!?! Why would this test be calling the internet?!?!

I was caught off guard by this as well.

The test above generates an HTML email that would get sent to the user. In testing mode, the email isn't sent, but has it's contents logged so we can inspect it with **caplog** and verify that the email we generated is valid and works.

All good, nothing leaving our system.

BUT. . .when we generate the HTML for that email, there are asset requests for CSS/etc that do go out to the internet.

So should we mock or prevent that from happening? Skip HTML generation? I'm not worrying about it for this one case at the moment, but knowing that this test calls out and being forced to make an intentional decision is very valuable in my mind.
