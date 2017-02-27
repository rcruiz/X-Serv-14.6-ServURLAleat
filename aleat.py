#!/usr/bin/python3

import webapp
import random


class aleat(webapp.webApp):
    """Generator random URLs with classes"""

    def parse(self, request):
        return None

    def process(self, parsedRequest):
        randomURL = str(random.randint(0, 1000000000000))
        newURL = "http://localhost:" + str(port) + "/" + randomURL
        return ("200 OK", "<html><body><p>Hola. " + '<a href="' + newURL +
                '">' + "Dame otra</a>" + "</p></body></html>")


if __name__ == "__main__":
    port = 1234
    testWebApp = aleat("localhost", port)
