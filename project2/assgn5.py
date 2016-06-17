fname = 'mbox-short.txt'
fh = open(fname)
sendersList = []
for line in fh:
    line = line.rstrip()
    if line.startswith('From: '):
        line = line.split()
        sendersList.append(line[1])

senders = dict()
for name in sendersList:
    senders[name] = senders.get(name, 0) + 1


senderMax = 'NONE'
maxVal = 0

for key, value in senders.items():
    if key != senderMax and value > maxVal:
        senderMax = key
        maxVal = value

print(senderMax, maxVal)
