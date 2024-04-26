#!/usr/bin/python3
"""
This script sends a request to the specified URL and
displays the value of the variable 'X-Request-Id' in the response header.
"""
import requests
import sys


if __name__ == "__main__":
    # Extract the URL from the command-line argument
    url = sys.argv[1]

    # Send the GET request
    response = requests.get(url)

    # Extract the value of 'X-Request-Id' from the response header
    x_request_id = response.headers.get('X-Request-Id')

    print(x_request_id)
