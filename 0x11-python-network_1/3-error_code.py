#!/usr/bin/python3
"""
This script sends a request to a specified URL and
displays the body of the response.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":

    url = sys.argv[1]       # Extract the URL from the command line argument

    req_obj = urllib.request.Request(url)

    try:
        # Send the request and open the response
        with urllib.request.urlopen(req_obj) as response:
            # Read and decode the response body in utf-8
            response_body = response.read().decode('ancii')

        print(response_body)

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
