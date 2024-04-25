#!/bin/bash

# Check if the URL is provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

# Store the URL in a variable
url="$1"

# Send the GET request using curl and get the response body and status code
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
status_code=${response: -3}
body=$(curl -s "$url")

# Check if the status code is 200 and print the body
if [ "$status_code" = "200" ]; then
    echo "$body"
fi
