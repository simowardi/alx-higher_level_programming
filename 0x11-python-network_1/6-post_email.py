#!/usr/bin/python3
"""
This script sends a POST request to the specified URL
with the email as a parameter and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    # Extract the URL from the command-line argument
    url = sys.argv[1]

    # Extract the email from the command-line argument
    email = sys.argv[2]

    # Send the POST request with email as a parameter
    response = requests.post(url, data={'email': email})

    # Display the body of the response
    print(response.text)
