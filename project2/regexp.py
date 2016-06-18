import re

fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if re.search('^From: ', line):
        print(line)
fh.close()

text = "From: lorem ipsum: spme more text"
y = re.findall('^F.+:',text)
print(y)
