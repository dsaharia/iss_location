import urllib.request # to make requests to the api
import json # to parse the json response
import reverse_geocoder as rg # to get address from location

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url) # request the api, returns a JSON object
json_result = json.loads(response.read()) # read the JSON object

# Separate different values based on keys.
people = json_result['people'] # people currently in space
number_in_space = json_result['number'] # total people in space
print("People in space : ", number_in_space)
print("----NAMES----")

for p in people:
	print(p['name'])

# ISS data
iss_url = "http://api.open-notify.org/iss-now.json"
iss_response = urllib.request.urlopen(iss_url)
iss_json_result = json.loads(iss_response.read())
# Store the positions
latitude = iss_json_result['iss_position']['latitude'] # store the latitude
longitude = iss_json_result['iss_position']['longitude']
print("Latitude: ", latitude," -- ", "Longitude: ", longitude)

address = rg.search((latitude, longitude)) # Get the address from location tuple returns a list
address_name = address[0]['name']
address_admin1 = address[0]['admin1']
address_admin2 = address[0]['admin2']
address_cc = address[0]['cc']
print("----Address----")
print(address_name, ", ", address_admin1, address_admin2, address_cc)