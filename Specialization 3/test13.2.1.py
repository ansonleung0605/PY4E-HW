# $ python3 solution.py
# Enter location: South Federal University
# Retrieving http://...
# Retrieved 2443 characters
#  Place id ChIJy0Uc1Zmym4gR3fmAYmWNuac

import urllib.error, urllib.request, urllib.parse
import json

target = 'http://py4e-data.dr-chuck.net/json?' 
local = input('Enter location: ')
url = target + urllib.parse.urlencode({'address': local, 'key' : 42})

print('Retriving', url)
data = urllib.request.urlopen(url).read()
print('Retrived', len(data), 'characters')
js = json.loads(data)
print(json.dumps(js, indent = 4)) 
print('Place id', js['results'][0]['place_id'])
