import os
os.chdir('/Users/leunglaphin/Desktop/PY4E/')
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 1:
        continue
    if wds[0] != "From":
        continue
    print(wds[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
