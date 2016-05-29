# create a file

fw = open('mini.txt', 'w')
fw.write('mini is awesome\nsorry..super awesome\n')
fw.close()

fr = open('mini.txt', 'r')
data = fr.read()
print(data)
fr.close()


