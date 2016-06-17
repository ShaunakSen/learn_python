bag = dict()
bag['chocolates'] = 10
bag['money'] = 100
bag['cards'] = 5
print(bag['cards'])
bag['cards'] += 2
print(bag)

mini = {'age': 21, 'loves': 'shona', 'likes':
    {
        'food': 'chocolates',
        'clothes': 'red dress'
    }}
print(mini)

if 'age' in mini:
    print(mini['age'])
else:
    print(0)

print(mini.get('likes', 0))

counts = dict()
list = ['mini', 'shona', 'drigger', 'mini', 'shona', 'dronzer', 'drigger', 'mini']
for name in list:
    counts[name] = counts.get(name, 0) + 1
print(counts)


for item in counts:
    print(item, counts[item])


print(bag.keys())
print(bag.values())

print(bag.items())

for a,b in bag.items():
    print(a, b)