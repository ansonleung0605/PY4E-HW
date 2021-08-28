name = input("Enter file:")
if len(name) < 1 : name = "/Users/aqumon/Desktop/Python Coding/PY4E Homework/mbox-short.txt"
handle = open(name)

maxauthor = dict()
for line in handle:
    for line in handle:
        line = line.rstrip()
        if not line.startswith("From "): continue
        word = line.split()
        email = word[5]
        time = email.split(":")
        hour = time[0]
        maxauthor[hour] = maxauthor.get(hour,0) + 1

hourslist = []
for k, v in maxauthor.items():
	hourslist.append( (k, v) )
hourslist.sort()
for k, v in hourslist:
	print(k,v)
            