import requests


base_url = "https://swapi.info/api/"

the_rest = "people/5"
verify_file = "C:\\Users\\augustinja\\Code\\DevAscDemo\\zscaler.pem"

response = requests.get(base_url + the_rest , verify= verify_file)
print(response.status_code)
print(type(response.json()))

g = (response.json()["films"])

for x in g:
    response1 = requests.get(x , verify= verify_file)

    print(response1.json()["title"])