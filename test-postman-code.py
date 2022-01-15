import requests

url = "https://198.18.1.10:8443/j_security_check"

payload = 'j_username=admin&j_password=admin'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
print(response.status_code)
print(response.cookies)
