#!/usr/bin/python3
import urllib.request


def fetch_url(url):
    """Fetches the status from a given URL using urllib.

    Args: url (str): The URL to fetch the status from.

    Returns: str: The body response content.
    """
    with urllib.request.urlopen(url) as responde:
        content = responde.read()

    return content


if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"

    # Fetch the status content from the URL
    status = fetch_url(url)

    print("Body response:")
    print(f"\t- type: {type(status)}")
    print(f"\t- content: {status}")
    print(f"\t- utf8 content: {status.decode('utf-8')}")
