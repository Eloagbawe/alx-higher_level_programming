#!/bin/bash
# This script sends a request to a URL passed as an argument, and displays only the status code of the response
curl  -sL -w '%{http_code}\n' -I "$1" -o /dev/null
