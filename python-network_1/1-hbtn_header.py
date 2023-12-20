''' displays value of X-Request-Id found in header of response  '''
import urllib.request as req
from sys import argv
import requests
import sys
if __name__ == "__main__":
    with req.urlopen(req.Request(argv[1])) as response:
        print(response.headers.get('X-Request-Id'))