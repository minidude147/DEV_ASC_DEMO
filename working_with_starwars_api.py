import requests
import json

url = "https://swapi.info/api/starships/3"

payload = {}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data= payload , verify = "C:\\Users\\augustinja\\Code\\DevAscDemo\\zscaler.pem")

print(payload)

requests.re
print(type(payload))




