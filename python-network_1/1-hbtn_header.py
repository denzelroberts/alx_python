''' displays value of X-Request-Id found in header of response  '''
import urllib.request as requests
from sys import argv
if __name__ == "__main__":
    with req.urlopen(requests.Request(argv[1])) as response:
        print(response.headers.get('X-Request-Id'))