#!/bin/bash

# This script sends a HEAD request to a given URL using curl
# and retrieves the size of the response body in bytes.

# Check if the URL is provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

# Store the URL in a variable
url="$1"

# Send the request using curl and get the response body size
body_size=$(curl -sI "$url" | grep -i 'Content-Length' | awk '{print $2}' | tr -d '\r')

# Print body size
echo "$body_size"
