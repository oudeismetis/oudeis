# Website for oudeis.co

A place for me to follow my thoughts in the open as I work on my projects.

Projects with source code are hosted where this code is hosted.

## Installation

Built with [Hugo](https://gohugo.io)

Follow the vanilla [setup instructions](https://gohugo.io/overview/installing/) after cloning the repo.

## Running

In order to see your site in action, run Hugo's built-in local server.

```
$ hugo server
```

To also see draft posts:

```
$ hugo server -D
```

Now enter [`localhost:1313`](http://localhost:1313) in the address bar of your browser.

## Configuration

Most config happens in the config.toml file.

## Deployment

Follow `deploy.sh` to get an idea

### Theme customized from the Nederburg theme

Nederburg is likely out of date. There is a [fork that is getting bug fixes](https://github.com/ayeks/hugo-nederburg-theme)

### Gravatar

To have an image in your author bio shown after posts, go to [Gravatar](https://gravatar.com/) and configure it and then add the email address that you have associated with it in the email section in settings:

```toml
email = "your@gravatar.email"
```

### Style customization

Most styles are provided by the Nederburg theme.

Overrides have been made in the `static/css/custom.css` file.

### Google Analytics

You can optionally enable Google Analytics.

```toml
googleAnalytics = "UA-XXXXX-X"
```

Leave the `googleAnalytics` key empty to disable it.

## License

The code for this site is released under the MIT License. (See the license file)

Opinions, tutorials, and descriptions about my projects on this website are liberally sharable under [Creative Commons](https://creativecommons.org/licenses/by-sa/4.0/).  

For the project ideas themselves and any code related to those projects, see the license file provided where the project is hosted.  

If you desire to use my work in a way not governed by the above, please contact me directly so we can work something out.  
