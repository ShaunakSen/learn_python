list = [1, 2, 'mini', [12, 13]]
for item in list:
    print(item)

list[0] = 13

print(list)

list2 = range(5)
print(list2)

friends = ['mini', 'paddy', 'pappi', 'saurav']
for i in range(len(friends)):
    print("Here's wishing friend no: ", i)
    print("Happy B'day ", friends[i])

stuff = []
print(stuff)

print('mini' in list)
print('mini' not in list)

listOfNums = []
while True:
    inp = input("Enter a no: ")
    if inp == 'done':
        break
    inp = float(inp)
    listOfNums.append(inp)

average = sum(listOfNums)/len(listOfNums)
print(average)

string = 'Shona Loves Mini Forever'
list3 = string.split()
print(list3)


