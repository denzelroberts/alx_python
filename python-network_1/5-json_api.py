"""CHECK"""

import requests
import sys

url = "http://0.0.0.0:5000/search_user"
letter = sys.argv[1] if len(sys.argv) > 1 else ""

payload = {"q": letter}
response = requests.post(url, data=payload)

try:
    json_data = response.json()
    if json_data:
        print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")