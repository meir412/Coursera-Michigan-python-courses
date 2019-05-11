
from urllib.request import urlopen
from urllib.parse import urlencode
import json

raw_url = 'http://py4e-data.dr-chuck.net/json?'

api_key = 42

address = input('Enter location: ')

parms = { 'address': address, 'key': api_key}

url = raw_url + urlencode(parms)

json_as_string = urlopen(url).read().decode()

json_as_dict = json.loads(json_as_string)

place_id = json_as_dict['results'][0]['place_id']

print(place_id)

print(url)
