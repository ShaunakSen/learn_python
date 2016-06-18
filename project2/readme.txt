Strings

    dir()
    this method lists all methods an object has
    .upper()
    .replace()
    greet = 'Hello Bob'
    greet.replace('Bob', 'Mini')

    Stripping whitespaces
    lstrip(), rstrip(), strip() -> both left and right


    prefix: startswith('string')
    .find()
    It has 3 params: 1st is str to find
    2nd and 3rd are optional: starting pos and end pos

    We have string string = 'From manishaagarwal838@gmail.com Mon July 13 2016'
    we want to find host name

    string = 'From manishaagarwal838@gmail.com Mon July 13 2016'
    apos = string.find('@')
    spos = string.find(' ', apos)
    host = string[apos + 1:spos]
    print(host)

FILES
    1.open()
    handle = open(filename, mode)
    returns a handle to manipulate file
    handle maintains connection betwn file and program
    stuff = "a\nb"
    len(stuff) = 3

    To read every line in a file:

    file = open('mini.txt')
    count = 0
    for line in file:
        print line
        count +=1
    print("no of lines: " + count)

    read entire file:
    .read()

    it returns string
    note: if file contains
    heyy mini
    how r ru
    This basically means
    heyy mini\n
    how r ru\n
    So this is what comes in the string

    fhand = open('mbox.txt')
    for line in fhand:
    if line.startswith('From:'):
        print(line)

    Output:
    From: stephen.marquard@uct.ac.za

    From: louis@media.berkeley.edu

    From: zqian@umich.edu

    From: rjlowe@iupui.edu

    From: zqian@umich.edu

    From: rjlowe@iupui.edu

    ......


    Where do these blank lines come from??

    When we read file each line ends in \n
    also print () causes a \n
    so there we have our extra line

    So how do we solve ds?
    recall rstrip() removes trailing whitespaces
    \n is also whitespace
    fhand = open('mbox.txt')
    for line in fhand:
        line = line.rstrip()
        if line.startswith('From:'):
            print(line)

    for line in fhand:
        line = line.rstrip()
        if not line.startswith('From:'):
            continue
        print(line)


    Look for lines which have '@uct.ac.za'
    for line in fhand:
        line = line.rstrip()
        if '@uct.ac.za' not in line:
            continue
        print(line)


    Another eg:
    fname = input(r'Enter file name: ')

    fhand = open(fname)

    count = 0
    for line in fhand:
        line = line.rstrip()
        if line.startswith('Subject:'):
            count += 1

    print('There were ', count, 'objects')
    fhand.close()

    ERROR CONTROL

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


LISTS

    A list is a collection
    A list element can be any Python object - even another list

    Strings are immutable.. we cant change contents of string
    string = 'mini'
    stringg[0] = 'M'
    ERROR!


    Lists are mutable
    list = [1, 2, 'mini', [12, 13]]
    list[0] = 13
    print(list)

    o/p:   [13, 2, 'mini', [12, 13]]

    len(list)..gets length

    Range: it generates a list
    range([start], stop[, step])
    list2 = range(5)
    print(list2)
    [0, 1, 2, 3, 4]
    The range function creates a sequential list of numbers.
    The code below generates a list containing all of the integers, up to 10.
    numbers = list(range(10))
    print (numbers)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(5):
      print("hello!")
    You don't need to call list on the range object when it is used in a for loop,
    because it isn't being indexed, so a list isn't required.

    The call to list is necessary because range by itself creates a range object,
    and this must be converted to a list if you want to use it as one.

    friends = ['mini', 'paddy', 'pappi', 'saurav']
    for i in range(len(friends)):
        print("Here's wishing friend no: ", i)
        print("Happy B'day ", friends[i])

    Concatenate lists by +
    But this is temporary
    to affect permanently u can use append
    slicing:same as strings

    print('mini' in list) -> True
    print('mini' not in list) -> False
    sort()
    max()
    min()
    sum()
    insert(index,element)
    index(element) -> returns index of the first occurrence that particular element.
    If the item isn't in the list, it raises a ValueError.

    list.count(obj): Returns a count of how many times an item occurs in a list
    list.remove(obj): Removes an object from a list
    list.reverse(): Reverses objects in a list

    words = ["Python", "fun"]
    index = 1
    words.insert(index, "is")
    print(words)

    listOfNums = []
    while True:
        inp = input("Enter a no: ")
        if inp == 'done':
            break
        inp = float(inp)
        listOfNums.append(inp)

    average = sum(listOfNums)/len(listOfNums)
    print(average)


    Note: float(inp)

    This is bcoz input always returns a STRING!!
    _________________________________________________________


    Now we could have written a simpler program for the above
    take vars count and sum..keep adding
    and do ave later
    not even though this would be having greater no of lines of code it will take up less memory

    STRINGS AND LISTS

    string = 'Shona Loves Mini Forever'
    list3 = string.split()
    print(list3)
    ['Shona', 'Loves', 'Mini', 'Forever']
    split() looks at many spaces as 1 single space
    hobbies = 'first;second;third'
    hobbies.split(';')


FUNCTIONS

    Any statement that consists of a word followed by information in parentheses is a function call
    Technically, parameters are the variables in a function definition,
    and arguments are the values put into parameters when functions are called.

    Like in javaScript functions can be assigned to variables

    def multiply(x, y):
      return x * y

    a = 4
    b = 7
    operation = multiply
    print(operation(a, b))

    Functions can also be used as Arguments to other functions

    def add(x, y):
        return x + y

    def do_twice(func, x, y):
      return func(func(x, y), func(x, y))

    a = 5
    b = 10

    print(do_twice(add, a, b))


    So we can use or call any function inside another

DICTIONARIES

    A dictionary is like an associative array in PHP

    bag = dict()
    bag['chocolates'] = 10
    bag['money'] = 100
    bag['cards'] = 5
    print(bag['cards'])
    bag['cards'] += 2
    print(bag)

    5
    {'cards': 7, 'chocolates': 10, 'money': 100}

    mini = {'age': 21, 'loves': 'shona', 'likes':
    {
        'food': 'chocolates',
        'clothes': 'red dress'
    }}
    print(mini)

    {'loves': 'shona', 'likes': {'food': 'chocolates', 'clothes': 'red dress'}, 'age': 21}

    Notice that the order in which u declare a dict in ur code may not be same order printed out
    This is bcoz internally, unlike in lists dicts are not stored in ordered form

    key in dict: true or false

    print('age' in mini)
    True

    if 'age' in mini:
        print(mini['age'])
    else:
        print(0)

    For this python has a built in method called get

    mini.get('age',0)

    0 signifies what value to return if that key is not found

    program to take in a list and count no of occurrences and put it in dict:

    counts = dict()
    list = ['mini', 'shona', 'drigger', 'mini', 'shona', 'dronzer', 'drigger', 'mini']
    for name in list:
        counts[name] = counts.get(name, 0) + 1
    print(counts)

    {'shona': 2, 'dronzer': 1, 'mini': 3, 'drigger': 2}

    For loops :
    for item in counts:
        print(item, counts[item])

    bag.keys() -> dict_keys(['chocolates', 'money', 'cards'])
    bag.values() -> dict_values([100, 7, 10])

    Note.. we cant predict order of either keys() or values() methods
    BUT these two WILL come out in SYNC AS LONG AS WE don no change dictionary between
    calling these 2 methods

    bag.items() -> dict_items([('chocolates', 10), ('cards', 7), ('money', 100)])

    for a,b in bag.items():
        print(a, b)

    chocolates 10
    cards 7
    money 100


TUPLES

    They are non changeable lists

    x = (1, 2, 3, 4)
    print(sum(x))
    10


    x[2] =6
    ERROR

    sort() append() reverse() DO NOT WORK with tuples

    as we cant change it ...


    we can only do count and index

    Tuples are more efficient.. they are faster and use less memory

    We can use them while making temp vars which we dont change

    a, b = (11, 12)
    print(a)

    mini = dict()
    mini['clothes'] = 100
    mini['chocolates'] = 200
    print(mini.items())

    dict_items([('clothes', 100), ('chocolates', 200)])

    We get back a list
    Each item in a list is a tuple of key, value

    mini = dict()
    mini['clothes'] = 100
    mini['chocolates'] = 200
    print(mini.items())

    for key, value in mini.items():
        print("Mini has", value, key)

    Mini has 100 clothes
    Mini has 200 chocolates

    Tuples are comparable
    print((0, 1, 2) < (0, 2, 5))
    True

    it compares one by one
    0 with 0 same so next
    1 with 2 -> true

    Sort by keys

    aDict = {'c':2, 'b':1, 'e':23,'a': 4}
    aList = aDict.items()
    print(sorted(aList))

    [('a', 4), ('b', 1), ('c', 2), ('e', 23)]\

    Sort by values(Descending Order)

    tempList = list()

    for k, v in sorted(aDict.items()):
        tempList.append((v, k))

    print(tempList)

    tempList.sort(reverse=True)
    print(tempList)

    [(23, 'e'), (4, 'a'), (2, 'c'), (1, 'b')]


    Most common words in a file

    fname = 'romeo.txt'
    fh = open(fname)
    wordsDict = dict()
    wordsList = list()
    for line in fh:
        line = line.rstrip()
        words = line.split()
        for word in words:
            wordsDict[word] = wordsDict.get(word, 0) + 1

    print(wordsDict)

    for k, v in wordsDict.items():
        wordsList.append((v, k))

    wordsList.sort(reverse=True)

    print(wordsList)
    fh.close()

    [(3, 'the'), (3, 'is'), (3, 'and'), (2, 'sun'), (1, 'yonder'), (1, 'with'), (1, 'window'),
    (1, 'what'), (1, 'through'), (1, 'soft'), (1, 'sick'), (1, 'pale'), (1, 'moon'), (1, 'light'),
    (1, 'kill'), (1, 'grief'), (1, 'fair'), (1, 'envious'), (1, 'east'), (1, 'breaks'), (1, 'already'),
    (1, 'Who'), (1, 'Juliet'), (1, 'It'), (1, 'But'), (1, 'Arise')]

    Note wordsList.sort(reverse=True) sorts based on key and then value


    List Comprehension

    print([ (v, k) for k, v in wordsDict.items() ])

    The outermost [  ] is a list comprehension
    It says construct dynamically a list of tuples (v, k)
    and (v, k) will be assigned according to: k, v in wordsDict.items()


    Now as we have list of tuples in val, key order we can sort them to get which word occurred most
    no of times



REGULAR EXPRESSIONS


    It is a programming language that specializes in string matching
    It is a language of characters, not tokens
    It was developed in 70s
    It is a mark of awesomeness!

    ^	Matches the beginning of a line
    $	Matches the end of the line
    .	Matches any character
    \s	Matches whitespace
    \S	Matches any non-whitespace character
    *	Repeats a character zero or more times
    *?	Repeats a character zero or more times (non-greedy)
    +	Repeats a character one or more times
    +?	Repeats a character one or more times (non-greedy)
    [aeiou]	Matches a single character in the listed set
    [^XYZ]	Matches a single character not in the listed set
    [a-z0-9]	The set of characters can include a range
    (	Indicates where string extraction is to start
    )	Indicates where string extraction is to end


    import re
    re.search(reg_expr, string_to_search_from)
    returns True or False

    import re
    fname = 'mbox-short.txt'
    fh = open(fname)
    for line in fh:
        line = line.rstrip()
        if re.search('From: ', line):
            print(line)

    This prints out all lines which CONTAIN 'From: '

    To prints out all lines which START WITH 'From: '

    ^X.*:
    Lines starting with X then any char any no of times then :
    Now modify it st : is last char
    ^X.*:$

    X-Sieve: ok
    X-kjhdk: ok
    X-Plane is behind schedule: ok

    We want to not allow 3rd one ie with blank spaces

    ^X-\S+:
    Starting with X- then one or more non blank chars and :
    3rd case we get X- but we get ' ' before : so does not select that

    If we want matching strings to be extracted, we use re.findall()..
    It finds all and puts in a list

    [0-9] -> accept single char in range 0-9
    [] is for single char
    [0-9]+
    accept single char in range 0-9 repeated one or more times(see the list above)

    [AEIOU] -> one or more uppercase vowels

    text = "From: lorem ipsum: spme more text"
    y = re.findall('^F.+:',text)
    print(y)
    ['From: lorem ipsum:']

    Why not ['From:']

    greedy prefers the larger string always

    Non Greedy matching: ^F.+?:


    Suppose we have :
    From louis@media.berkeley.edu Thu Jan  3 17:18:23 2008

    we want: louis@media.berkeley.edu

    logic: find @ then go outward until u find ' '
    \S+@\S+
    so find @ sign and push outward until u find blank


    We can fine tune this further:

    ^From (\S+@\S+)


    so we match lines starting with From. Then a blank. Then one or more non blank chars. Then @. Then one
    or more non blank chars

    () signify which stuff to return back
    So even though the reg expr matches lines starting with From and... it only returns part within ()

    ie it only returns ['louis@media.berkeley.edu']


    now we only wanna get domain

    @([^ ]*)

    start.. get @.. then start extracting and check for any no of non blank chars..

    [^ ] -> match a non blank char
    [^ ]* ->match many non blank chars

    From .*@([^ ]*)

    start with From then blank then any no of chars then @ then start extracting

    We want to match lines of form:

    X-DSPAM-Confidence: 0.6959


    ^X-DSPAM-Confidence: ([0-9.]+)

    This is reg expr
    It searches lines starting with ^X-DSPAM-Confidence:
    Then starts extracting
    it matches one or more characters consisting of digits or .
    Basically it returns 0.6959 stuff

    Full code:

    import re

    fname = 'mbox-short.txt'

    fh = open(fname)
    numlist = list()
    for line in fh:
        line = line.rstrip()
        stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
        if (len(stuff) > 0):
            num = float(stuff[0])
            numlist.append(num)


    print(max(numlist))
    fh.close()

    0.9907


    if u wanna match something like $10.00

    \$[0-9.]+

    \ signifies $ is not a wild card here but part of string


















