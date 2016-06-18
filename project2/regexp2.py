import re

fname = 'mbox-short.txt'

fh = open(fname)
numlist = list()
for line in fh:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if (len(stuff) > 0):
        num = float(stuff[0])
        numlist.append(num)


print(max(numlist))
fh.close()
