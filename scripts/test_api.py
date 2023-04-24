import os
from urllib.parse import urlencode

import requests


TOKEN = os.getenv('SATURN_TOKEN')
url = "https://w-produ-midjourney-c0f227105bfc4b04885d1d9d77b5a179.internal.saturnenterprise.io:8000/generate_image"
headers = {"Authorization": f"token {TOKEN}"}
uu = url + "?" + urlencode({"prompt": "flying unicorn"})
print(uu)
response = requests.post(uu, headers=headers)
print(response)

with open("/homejovyan/image.png", "wb+") as f:
    f.write(response.content)