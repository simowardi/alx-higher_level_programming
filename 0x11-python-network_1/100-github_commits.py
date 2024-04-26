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
    repo = sys.argv[1]
    owner = sys.argv[2]
 
    # Construct the API URL using the repository and owner names
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    # Make a GET request to the GitHub API
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10] # Get the most recent 10 commits

        for commit in commits:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f"{sha}: {author}") # Print commit SHA and the author name
    else:
        print("Error retrieving commits")
