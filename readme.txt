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







