#!/usr/bin/python3
"""
This script sends a POST request with an email parameter
to a specified URL and displays the response body.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]       # Extract the URL from the command line argument
    email = sys.argv[2]     # Extract the email from the command line argument

    # Encode email into bytes
    data = urllib.parse.urlencode({'email': email}).encode('ascii')

    # Create Request object with URL and data
    req_obj = urllib.request.Request(url, data)

    try:
        with urllib.request.urlopen(req_obj) as response:
            # Read and decode the response body in utf-8
            response_body = response.read().decode('utf-8')
            print(response_body)

    except urllib.error.URLError as e:
        print(f"An error occurred: {e.reason}")
        sys.exit(1)
