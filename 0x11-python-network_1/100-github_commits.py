#!/usr/bin/python3
"""This script list 10 commits (from the most recent to oldest)
of the github repository “rails” by the user “rails”
"""

import requests
import sys

if __name__ == "__main__":
    repository = sys.argv[1]
    user = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repository)
    r = requests.get(url)
    res = r.json()

    for i in range(0, 10):
        print("{}: {}".format(res[i].get('sha'),
              res[i].get('commit').get('author').get('name')))
