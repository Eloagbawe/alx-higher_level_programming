#!/usr/bin/python3
"""This script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get('https://api.github.com/users/{}'.format(username), data={'auth': password})
    res = r.json()
    print(res.get('id'))
