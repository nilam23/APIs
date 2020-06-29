import urllib.request
import json

url1="http://api.open-notify.org/iss-now.json"
response1=urllib.request.urlopen(url1)
result1=json.loads(response1.read())

latitude=result1['iss_position']['latitude']
longitude=result1['iss_position']['longitude']

print('--ISS CURRENT LOCATION--')
print('Latitude: ', latitude)
print('longitude', longitude)

url2="http://api.open-notify.org/astros.json"
response2=urllib.request.urlopen(url2)
result2=json.loads(response2.read())


people_info=result2['people']
number_of_poeple=result2['number']
print("No of people in space currently: ", number_of_poeple)
print("--Names of Poeple in Space--")

for i in people_info:
	print(i['name'])