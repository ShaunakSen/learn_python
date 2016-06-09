print(r"C:\shaunak\noNo");
r->print out the raw string

Access indv characters from string

mini = " little mini"
mini[-1] = i
mini[-2] = n

mini[startPos:stopPos]

>>> len(mini)
11

LISTS
____

>>> players = [13, 16, 26, 4, 8]
>>> players[2]
26
>>> players[2]=28
>>> players
[13, 16, 28, 4, 8]
>>> players + [5, 23]
[13, 16, 28, 4, 8, 5, 23] // temporary concatenation
>>> players
[13, 16, 28, 4, 8]
>>> players.append(120) // permanent concatenation
>>> players
[13, 16, 28, 4, 8, 120]
>>> players[:2]
[13, 16]
>>> players[:2] = [1, 2] //change multiple values at once
>>> players
[1, 2, 28, 4, 8, 120]
>>> players[:2] = [] ///delete first 2 elements
>>> players
[28, 4, 8, 120]
>>> players[:] = []
>>> players
[]
_____________________________________________________________________

Keyword Arguments

def miniSentence(name="mini", action="likes", item="shona"):
    print(name, action, item)


miniSentence()
miniSentence(action="shops for", item="clothes")

Flexible no of arguments

def addNumbers(*args):
    total = 0
    for a in args:
        total += a

    print(total)


addNumbers(2, 3, 3)

Unpacking Arguments

def healthCalculator(age, apples, ciggerates):
    age = (100 - age) + (apples * 3.5) - (ciggerates * 2)
    print(age)


data = [22, 10, 0]
healthCalculator(data[0], data[1], data[2])
healthCalculator(*data)

Gives same result. It unpacks arguments from list and passes them into function


Sets

A collection of items but cant have any duplicates like lists can

Dictionaries

They are key-value pairs

Modules

Cool functionalities u can use
import module_name
To download a module:
settings->project interpreter->+


Reading and Writing from files

fw = open('mini.txt', 'w')
fw.write('mini is awesome\nsorry..super awesome\n')
fw.close()

fr = open('mini.txt', 'r')
data = fr.read()
print(data)
fr.close()


Downloading files from web

We want to download a csv file
this file : http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=4&e=29&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv

read start5.py


Make A Web Crawler!!

Install beautifulsoup4 package
it can go through all the website data. it can do cool stuff like getting the links and all

see script6.py

now this crawler can crawl a site give info about links

we want a crawler to crawl a site gather links visit the sites in the links and recursively keep doing that

see script6.py

Exception Handling

tuna = input('Whats your fav no \n')
print(tuna)

if user enters string error occurs

This is not syntax error.. this is exception.. It is called ValueError

ValueError occurs when user types something which cant be converted to int

while True:
    try:
        number =  int(input('Enter fav no: \n'))
        print(10/number)
        break
    except ValueError:
        print('Make sure u enter a no \n')

    except ZeroDivisionError:
        print('Dont pick 0 \n')

    except:
        break

    finally:
        print('Executes no matter what \n')


CLASSES AND OBJECTS

class Enemy:
    life = 3

    def attack(self):
        print('Ouch !')
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")

enemy1 = Enemy()
enemy1.attack()
enemy1.checkLife()

enemy2 = Enemy()
enemy2.attack()
enemy2.checkLife()

Here to access class vars inside class functions we have to use self


Init - gets called automatically when object is created
It is called first
Like a constructor

Class Var vs Instance Var

class Girl:
    gender = 'female'
    def __init__(self, name):
        self.name = name


mini = Girl('mini')
mini2 = Girl('budhhu mini')
print(mini.gender)
print(mini2.gender)
print(mini.name)
print(mini2.name)

The var gender is a class var
name is instance var
class var is same for all objects
Instance var is different for each object

INHERITANCE

class Parent:

    def print_last_name(self):
        print('Sen')


class Child(Parent):

    def print_first_name(self):
        print('Shaunak')


shaunak = Child()

shaunak.print_first_name()
shaunak.print_last_name()



Overriding a function

class Parent:

    def print_last_name(self):
        print('Sen')


class Child(Parent):

    def print_first_name(self):
        print('Shaunak')
    def print_last_name(self):
        print('blaaah blaaah')


shaunak = Child()

shaunak.print_first_name()
shaunak.print_last_name()


Multiple Inheritance


class Mario():
    def move(self):
        print('Mario Moving....')


class Shroom():
    def eat_shroom(self):
        print('Mario is BIG !!')


class BigMario(Mario, Shroom):
    pass

mini = BigMario()
mini.move()
mini.eat_shroom()

Word Counter

Crawl a web page .. get all words and show how frequently a word is used


First we get each word from titles in https://thenewboston.com/forum/recent_activity.php

import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    wordList = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('a', {'class':'title'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            print(each_word)
            wordList.append(each_word)


start('https://thenewboston.com/forum/recent_activity.php')

Now here there may be words like questions... or :) or some other strange symbols we dont need
we need to clean that up

def clean_up_list(wordlist):
    cleanWordList = []
    for word in wordlist:
        symbols = "!@#$%^&*()_\"+<>-.,?/:;{}[]|"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            print(word)
            cleanWordList.append(word)



Now we have to create a dictionary to store how often these words appear

Note we imported operator.. this allows us to work with built in data types in python


def create_dictionary(cleanWordList):
    word_count = {}
    for word in cleanWordList:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # sort dictionary

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)


    Now dictionary is comprised of key and value

    itemgetter(1) means sort by value
    itemgetter(0) means sort by key



Unpacking Lists

items = ['November 16, 2015', 'Clothes for Mini', 2000]

We want to separate the individual values in the list into variables


data1 = item[0]
data2 = item[1]
data3 = item[2]

But can we do it in one single line?

date, item, price = items
print(item)


Rule: make sure that no of vars = no of args n list

Now here we have to kno how many elements are in list

For example we have some lists of grades
They are all of variable length. We want to drop 1st and last grade and average all in between

first, *middle, last = grades

first will be grades[0] last will be last element

middle will be another list comprising the elements  in between

def drop_first_last(grades):
    first, *middle, last = grades
    average = sum(middle) / len(middle)
    print(average)


drop_first_last([65, 76, 98, 65, 21])
drop_first_last([65, 76, 100, 23, 98, 65, 21])


ZIP function

We have 2 lists of equal no if items and we will zip them together


print("Zipping Example")

first = ['mini', 'shona', 'pappi']
last = ['sen', 'sen', 'sarkar']

full_name = zip(first, last)

for name in full_name:
    print(name)

for fname, title in full_name:
    print(fname, title)

When we zip,

full_name = [('mini', 'sen'),('shona', 'sen'),('pappi', 'sarkar')]

LAMBDA

lambda is a small function which has no name

lamdba input: expression

answer = lambda x: x*7
print(answer(5))

When to use this?
Button(text="Click Me", command=lamdba:custom)

We dont wand to allocate separate function
Its something that happens once only
Like anonymous function in js

Get Min , Max of dictionary and sort dictionary

stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'APPL': 99.76
}

stocks_list = zip(stocks.values(), stocks.keys())
minimumValue = min(stocks_list)
print(minimumValue)

print(sorted(zip(stocks.values(), stocks.keys())))


first we consider dictionary into a joined list using zip
Then we use min and sorted methods









