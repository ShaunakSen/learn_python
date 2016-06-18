import re

fname = 'actual.txt'

fh = open(fname)
numlist = list()

for line in fh:
    line = line.rstrip()
    words = re.findall('([0-9]+)', line)
    if len(words) > 0:
        for word in words:
            numlist.append(int(word))
print(sum(numlist))

fh.close()
