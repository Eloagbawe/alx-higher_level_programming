#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL
and displays the body of the response
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        r = requests.get(url)
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.status_code))
