#!/usr/bin/python3
"""
This script takes in a letter,
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter,
and then displays the response.
"""
import requests
import sys


if __name__ == "__main__":
    # Extract the letter command-line argument
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    # Send a POST request with the letter as a parameter
    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        # Extract and decode the JSON response
        result = response.json()

        # Check if the JSON is empty
        if len(result) == 0:
            print("No result")

        # Check if the JSON is not empty and properly formatted
        elif 'id' in result and 'name' in result:
            print("[%d] %s" % (result['id'], result['name']))

    # Handle invalid JSON formatting
    except ValueError:
        print("Not a valid JSON")
