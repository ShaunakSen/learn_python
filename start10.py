items = ['November 16, 2015', 'Clothes for Mini', 2000]
date, item, price = items
print(item)


def drop_first_last(grades):
    first, *middle, last = grades
    average = sum(middle) / len(middle)
    print(average)


drop_first_last([65, 76, 98, 65, 21])
drop_first_last([65, 76, 100, 23, 98, 65, 21])

print("Zipping Example")

first = ['mini', 'shona', 'pappi']
last = ['sen', 'sen', 'sarkar']

full_name = zip(first, last)

for name in full_name:
    print(name)

for fname, title in full_name:
    print(fname, title)


