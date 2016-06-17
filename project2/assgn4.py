fname = 'mbox-short.txt'
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    print(email)
    count += 1

print("There were", count, "lines in the file with From as the first word")