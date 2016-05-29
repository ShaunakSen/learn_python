def miniSentence(name="mini", action="likes", item="shona"):
    print(name, action, item)


miniSentence()
miniSentence(action="shops for", item="clothes")


def addNumbers(*args):
    total = 0
    for a in args:
        total += a

    print(total)


addNumbers(2, 3, 3)


def healthCalculator(age, apples, ciggerates):
    age = (100 - age) + (apples * 3.5) - (ciggerates * 2)
    print(age)


data = [22, 10, 0]
healthCalculator(data[0], data[1], data[2])
healthCalculator(*data)
