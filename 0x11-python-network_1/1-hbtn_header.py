#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id
variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    # get url from Comend line
    url = sys.argv[1]

    # Create a Request object for the specified URL
    req_obj = urllib.request.Request(url)

    with urllib.request.urlopen(req_obj) as response:
        # Get the `X-Request-Id` value from the response headers
        request_id = response.headers.get('X-Request-Id')

        if request_id:
            print(request_id)
