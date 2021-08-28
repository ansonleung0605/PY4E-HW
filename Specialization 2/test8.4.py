import os
os.chdir('/Users/leunglaphin/Desktop/PY4E/')
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
    lst.sort()
print(lst)
