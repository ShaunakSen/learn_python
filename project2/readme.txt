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







