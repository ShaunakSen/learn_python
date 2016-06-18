x = (1, 2, 3, 4)
print(sum(x))

dir(x)

a, b = (11, 12)
print(a)

mini = dict()
mini['clothes'] = 100
mini['chocolates'] = 200
print(mini.items())

for key, value in sorted(mini.items()):
    print("Mini has", value, key)

print((0, 1, 2) < (0, 2, 5))

aDict = {'c': 2, 'b': 1, 'e': 23, 'a': 4}
aList = aDict.items()
print(sorted(aList))

tempList = list()

for k, v in sorted(aDict.items()):
    tempList.append((v, k))

print(tempList)

tempList.sort(reverse=True)
print(tempList)

fname = 'romeo.txt'
fh = open(fname)
wordsDict = dict()
wordsList = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        wordsDict[word] = wordsDict.get(word, 0) + 1

print(wordsDict)

for k, v in wordsDict.items():
    wordsList.append((v, k))

wordsList.sort(reverse=True)

print(wordsList[:])

print([(v, k) for k, v in wordsDict.items()])

fh.close()
