#!/usr/bin/python3
"""
This script makes a displays a response and handles http errors.
"""
import sys

import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
