fh = open('mbox-short.txt')

for line in fh:
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])