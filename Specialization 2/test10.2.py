name = input("Enter file:")
if len(name) < 1 : name = "/Users/aqumon/Desktop/Python Coding/PY4E Homework/mbox-short.txt"
handle = open(name)


d = dict()
for line in handle:
    if line.startswith("From "):
        line = line.rstrip()
        words = line.split()
        time = words[5]
        hour = time[0:2]
        d[hour] = d.get(hour,0) +1


newlist = []

for k,v in d.items():
    newlist.append((k,v))
newlist.sort()

for k,v in newlist:
    print(k,v)
