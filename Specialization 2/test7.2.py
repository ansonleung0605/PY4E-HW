# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
hey = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    j = line.find("0")
    line = float(line[20:])
    hey = hey + line
    count = count + 1
print("Average spam confidence: " + str(hey/count))
