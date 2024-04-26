#!/usr/bin/python3
"""
This script takes your GitHub credentials
(username and personal access token),
uses the GitHub API with Basic Authentication,
and displays your user ID.
"""
import requests
import sys


if __name__ == "__main__":
    # Extract the username and personal access token
    username = sys.argv[1]
    password = sys.argv[2]

    # Create the auth token in the format "username:personal_access_token"
    auth = (username, password)

    # Create the headers for the request
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }

    # Send a GET request to fetch user details using Basic Authentication
    r = requests.get('https://api.github.com/user', headers=headers, auth=auth)

    # Extract and decode the JSON response
    result = r.json()

    # Display the user ID if the request was successful
    if r.status_code == 200:
        print(result['id'])
    else:
        print(None)
