import requests

r = requests.get('https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers').json()
for i in r['providerList']:
    print(i)





'''
Structure of JSON: 

{'id': , vaccineBrands: { : }, contact: {phone: }, hours: , address: }

'''

#vaccineBrands is for brand: in stock/call to confirm


