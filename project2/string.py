string = 'From manishaagarwal838@gmail.com Mon July 13 2016'

apos = string.find('@')
spos = string.find(' ', apos)
host = string[apos + 1:spos]
print(host)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos + 3])

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)

text = "X-DSPAM-Confidence:    0.8475"
len = len(text)
start = text.find(' ')
text2 = text[start:len]
text3 = text2.lstrip()
print(text3)

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

fhand.close()

print("SECOND EXAMPLE...")

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
fhand.close()

print("\n\nLooking for '@uct.ac.za'\n\n")

fhand = open('mbox.txt')

for line in fhand:
    line = line.rstrip()
    if '@uct.ac.za' not in line:
        continue
    print(line)

fhand.close()

print("\n\nLooking for no of line starting with 'Subject:' \n\n")

fname = input(r'Enter file name: ')
try:
    fhand = open(fname)

except FileNotFoundError:
    print('whooops')
    exit()

count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('Subject:'):
        count += 1

print('There were ', count, 'objects')
fhand.close()
