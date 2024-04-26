#!usr/bin/python3
"""
This script retrieves the 10 most recent commits from a GitHub repository
and prints them in a specific format.
(from the most recent to oldest)
The repository and owner names are passed as command line arguments.
Usage: ./100-github_commits.py <repository> <owner>
Example: ./100-github_commits.py rails rails
"""
import requests
import sys


if __name__ == "__main__":
    # Get the repository and owner names from the command line arguments
    # Construct the API URL using the repository and owner names
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    # Make a GET request to the GitHub API
    response = requests.get(url)

    # Retrieve the JSON data from the response
    commits = response.json()

    # Iterate over the first 10 commits (if available)
    for commit in commits[:10]:
        # Get the commit ID
        commit_id = commit.get("sha")
        # Get the author name
        author_name = commit.get("commit").get("author").get("name")

        # Print the commit ID and author name
        print(f"{commit_id}: {author_name}")
