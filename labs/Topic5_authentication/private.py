import requests
import json
from config import config2 as cfg

filename = "repos-private.json"

repository_name = "mhmdmahdi/aprivateone"
url = f"https://api.github.com/repos/{repository_name}"

apikey = cfg["apikey"]

response = requests.get(url, auth=('token', apikey))
print(response.status_code)
#print (response.json())

with open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)