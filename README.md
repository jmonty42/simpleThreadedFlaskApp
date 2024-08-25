# Simple Flask app with threading

Got an interesting interview question that stumped me pretty hard and wanted to flesh it out afterwards, so this is it.

## Requirements

Create a single app that has two running servers, one that listens for requests on port 4000 and the other that listens on port 5000. The first one will respond to `get` requests on the path `/test` by sending 10 `get` requests to the second service in parallel.

Clean everything up gracefully when `SIGINT` is received.

## Approach

With some prodding I went with trying to create a simple Flask app with threading. My previous employer used Flask, but I had never worked with it directly from the point of a brand new app. I don't think the interview went very well, but I wanted to flesh it out to be more familiar with the ideas and stack for the future.