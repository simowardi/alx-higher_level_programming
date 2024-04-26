#!/usr/bin/python3
"""Fetches the status from a given URL using urllib"""
import urllib.request


if __name__ == '__main__':

    url = "https://alx-intranet.hbtn.io/status"

    # Fetch the status content from the URL
    with urllib.request.urlopen(url) as response:
        status = response.read()

    print("Body response:")
    print(f"\t- type: {type(status)}")
    print(f"\t- content: {status}")
    print(f"\t- utf8 content: {status.decode('utf-8')}")
