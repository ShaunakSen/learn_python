fname = 'mbox-short.txt'

words = list()
wordsDict = dict()
tempList = list()

fh = open(fname)
for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        words = words[5]
        words = words.split(':')
        for word in words[0:1]:
            wordsDict[word] = wordsDict.get(word, 0) + 1

for k, v in wordsDict.items():
    tempList.append((k, v))

tempList.sort()

for k, v in tempList:
    print(k, v)
fh.close()
