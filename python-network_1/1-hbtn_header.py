''' displays value of X-Request-Id found in header of response  '''
import requests
import sys
import urllib.request as requests
from sys import argv
if __name__ == "__main__":
    with requests.urlopen(requests.Request(argv[1])) as response:
        print(response.headers.get('X-Request-Id'))