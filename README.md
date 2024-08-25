# Simple Flask app with threading

Got an interesting interview question that stumped me pretty hard and wanted to flesh it out afterwards, so this is it.

## Requirements

Create a single app that has two running servers, one that listens for requests on port 4000 and the other that listens on port 5000. The first one will respond to `get` requests on the route `/test` by sending 10 `get` requests to the second service's `/test` route in parallel.

Clean everything up gracefully when `SIGINT` is received.

## Approach

With some prodding I went with trying to create a simple Flask app with threading. My previous employer used Flask, but I had never worked with it directly from the point of a brand new app. I don't think the interview went very well, but I wanted to flesh it out to be more familiar with the ideas and stack for the future.

## Running

I used JetBrains' PyCharm for this app, so it handles setting up the venv with dependencies. I did use PyCharm to capture the versions of these dependencies in `requirements.txt` so that one could just use pip to install them.

After the requirements are installed just running `python app.py` will launch the app with the two servers running:

```
$ .venv/bin/python app.py
Server 1 is running...
 * Serving Flask app 'server1'
 * Debug mode: off
Server 2 is running...
 * Serving Flask app 'server2'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:4000
Press CTRL+C to quit
```