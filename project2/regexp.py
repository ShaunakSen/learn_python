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

a = 'From: Using the : character'
b = re.findall('^F.+:', a)

print(b)

a= 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
b = re.findall('\S+?@\S+',a)
print(b)