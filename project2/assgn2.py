fname = 'mbox-short.txt'
fh = open(fname)
count = 0
lines = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        requiredLine = line
        colonPos = requiredLine.find(':')
        decimalPos = requiredLine.find('.')
        requiredLine = requiredLine[colonPos + 1:len(requiredLine)]
        requiredLine = requiredLine.lstrip()
        count += float(requiredLine)
        lines += 1

average = float(count/lines)
print (average)



