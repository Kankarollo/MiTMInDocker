""" 
Block URLs matching a regex, by just returning an HTTP 404 code. As addons can be called with an argument,
the file containing the URLs is hardcoded, but could be extracted from an environment variable for example.

Unfortunately in Python, contrary to Rust, you can't define a regex set and try to match any regex for a string.

"""
import re
import os
from mitmproxy import http
from mitmproxy import ctx

class BlockResource:
    def __init__(self):
        # define a new list for holding all compiled regexes. Compilation is done once when the addon
        # is loaded
        self.urls = []

        url_path = "/home/mitmproxy/.mitmproxy/urls.txt"
        # read the configuration file having all string regexes
        for re_url in open(url_path):
            self.urls.append(re.compile(re_url.strip()))

        # log how many URLS we have read
        ctx.log.info(f"{len(self.urls)} urls read")

    def response(self, flow):
        # test if the request URL is matching any of the regexes
        if any(re.search(url, flow.request.url) for url in self.urls):
            ctx.log.info(f"found match for {flow.request.url}")
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                '<html><body><img src="https://i.pinimg.com/originals/db/78/59/db7859a804968062c5fade4efef1827a.jpg"/></body></html>',
                {"Content-Type": "text/html"} 
            )

addons = [
    BlockResource()
]
