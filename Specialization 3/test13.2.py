import urllib.request as ur
import json
url = "http://py4e-data.dr-chuck.net/comments_348676.json"
print("Retriving", url)
data = ur.urlopen(url).read().decode()  #string from utf-8 to unicode
print('Retrieved', len(data), 'characters')

object = json.loads(data)

total = 0
number = 0
for comment in object["comments"]:
    total += int(comment["count"])
    number += 1
print("total", total)
print("number", number)
