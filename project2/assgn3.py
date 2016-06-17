fname = 'romeo.txt'
fh = open(fname)
finalWords = []
for line in fh:
    line = line.rstrip()
    print(line)
    words = line.split()
    print(words)
    for word in words:
        if not word in finalWords:
            finalWords.append(word)
            finalWords.sort()

print(finalWords)

