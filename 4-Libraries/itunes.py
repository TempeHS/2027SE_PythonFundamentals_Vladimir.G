import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("..." + sys.argv[1])
o = response.json()
for result in o["results"]:
    print(result["..."])
