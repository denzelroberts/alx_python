'''  sends a POST request to passed URL and displays response  '''
import requests
import sys
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    data = {'email' : argv[2]}
    data = argv.urlencode(data)
    data = data.encode('ascii')
    req = requests.Request(url, data)
    with requests.urlopen(req) as res:
        print(res.read().decode('utf-8'))
