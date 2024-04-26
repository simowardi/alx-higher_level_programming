#!/usr/bin/python3
"""
This script sends a request to the specified URL
and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
it prints "Error code:" followed by the value of the HTTP status code.
"""
import requests
import sys


if __name__ == "__main__":
    # Extract the URL command-line argument
    url = sys.argv[1]

    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the HTTP status code is greater than or equal to 400
    # Print the error code
    # else Displaythe body of the response
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
