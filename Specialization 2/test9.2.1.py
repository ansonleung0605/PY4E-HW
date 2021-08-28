name = input("Enter file:")
if len(name) < 1 : name = "/Users/aqumon/Desktop/Python Coding/PY4E Homework/mbox-short.txt"
handle = open(name)

maxauthor =dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith("From "): continue

    word = line.split()
    #print(word)
    maxauthor[word[1]] = maxauthor.get(word[1], 0)+1
largest = None
thelargestvalue = None

for k,v in maxauthor.items():
    if largest is None or v > thelargestvalue:
        largest = k
        thelargestvalue = v

print(largest, thelargestvalue)        



