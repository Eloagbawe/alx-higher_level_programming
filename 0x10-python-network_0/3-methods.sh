#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept
curl -sI -X OPTIONS "$1" | sed -n '2 p' | cut -c8-
