"""
Shared utility functions for the legal citation parser.
"""

import requests

def check_url(url):
    """
    Checks if a URL is valid by sending a GET request and verifying the status code.

    Args:
        url (str): The URL to check.

    Returns:
        str: The URL if it is valid, otherwise None.
    """

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return url
        else:
            return None
    except requests.RequestException:
        return None

