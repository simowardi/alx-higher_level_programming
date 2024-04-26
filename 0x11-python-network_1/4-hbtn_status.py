#!/usr/bin/python3
"""
This script fetches the URL https://alx-intranet.hbtn.io/status
and displays the body of the response.
"""
import requests


if __name__ == "__main__":
    # Define the URL
    url = "https://alx-intranet.hbtn.io/status"

    # Send the GET request
    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
