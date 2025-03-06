base_url = "https://api.fastforex.io/fetch-all?api_key=ac08e3afca-7bf7efc700-sskmuv"
import requests
response = requests.get(base_url)
response.ok
response.status_code
response.text
response.json()
type(response.json())
import json
json.dumps(response.json(), indent = 4)
response.json().keys()
print(json.dumps(response.json(), indent = 4))
param_url = base_url + "&from=USD&to=EUR,GBP,CHF,NGN"
response = requests.get(param_url)
data = response.json()
print('Data==>: ', data)
data
data['base']
data['results']
print('data[results]:=> ', data['results'])
# data['rates']
print('data[base]:=> ', data['base'])

print('data[results][NGN]:=> USD->NGN', data['results']['NGN'])

data = requests.get(param_url)
print('Data = requires.get(param_url): ', data)

