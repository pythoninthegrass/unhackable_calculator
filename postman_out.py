import requests

url = "https://app.cloud-logon.com/dev/easy_mode"

payload={}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
