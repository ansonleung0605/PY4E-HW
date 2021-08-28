import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = "http://py4e-data.dr-chuck.net/comments_348675.xml"
xml = urllib.request.urlopen(url).read()
print('Retrieving', url)
print('Retrieved', len(xml), 'characters')


root = ET.fromstring(xml)

lst = root.findall('.//count')
print('count', len(lst))
total = 0

for num in lst:
    total = total + int(num.text)
print(total)