import re
name = "/Users/aqumon/Desktop/Assignment/ActualData.txt"
file =open(name)

sum = 0
count = 0

for line in file:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    for n in num:
        n = int(n)
        sum = sum + n
        count += 1
        #print(count, ":" , n)
print(sum)