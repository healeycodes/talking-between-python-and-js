# Talking to Python from JavaScript (and Back Again!)

This repository contains the tutorial code for my article on communicating between Python and JavaScript.

<br>

![Desktop](https://github.com/healeycodes/talking-between-python-and-js/blob/master/header.png)

<br>

### Via JSON

A Flask web app with two routes. `/test` which serves a page with JavaScript that uses the Fetch API to GET JSON data from `/hello`, and then POSTs JSON data, also to `/hello`. Everything is logged to console.

Any issues with launching the Flask app should seek these [docs](http://flask.pocoo.org/docs/1.0/cli/), and the Flask home page for general installation instructions.

<br>

### Via processes

There's also some files that demonstrate how processes can communicate via the stdout. Data is reported by a spawn process which is caught and collected. This is displayed in Python and Node.js. `sensor.js`, `sensor.py`, `temperature-listener.js`, `temperature-listener.py`. With the Node.js parent process, events are used. For the Python parent process we use a simple buffer and check for the newline char.

<br>

Hopefully this repository (combined with the article) will answer some beginner questions about how different languages 'talk' to each other! I'm accepting any PRs that bring further clarity or fix errors.

<br>

MIT license.
