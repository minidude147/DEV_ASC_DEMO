import requests
import json


base_url = "https://swapi.info/api/"

verify_file = "C:\\Users\\augustinja\\Code\\DevAscDemo\\zscaler.pem"

endpoint = "people/1"



response = requests.get(base_url + endpoint , verify= verify_file )


data  = response.text

json_dict = json.loads(data)

print(type(json_dict))
print(json_dict)
print(json_dict["films"][2])