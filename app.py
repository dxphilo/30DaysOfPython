
# print ('I am john philip')
# print('o----')
# print('||||')
# print('*' * 10)
# Python Variables booleans, integers, floating point numbeers
# price =10
# rating = 4.9
# is_published = False
# print(price + rating)


# DAY TWO.

# capture input from the user and print it back

# name = input('please enter your name ')

# print('Hi ' + name + " thanks for coming over here")

# simple exercise ask two questions form the user and persona name and favourite colour and print them back.

# name = input('What is your name ')
# favColor = input('What is your favourite colors ')

# print('Hi ' + name + " " + favColor + " if your favourite colour")
# type of variables

# birth_year = input('Enter your birth year ')
# your_age = 2021 - int(birth_year)

# print("You are " + str(your_age) + " years old")


# program that asks that aske the users their weight and donverts it into kilograms
# print the answer to the terminal.

# user_weight = input('Enter your weight in pounds ')
# weight = int(user_weight)

# user_Kiloweight = weight *  0.453592

# print(user_Kiloweight)

# contatenations
# course = 'Python for "beginners"'
# print(course)

# course = "Python for 'beginners'"
# print(course)
# strings tha expands many lines, can both be singel or double qoutes.

# course = '''
# Hi Mosh Hamedani,

# Here is our initial email to you.


# Thank you.

# From the support Team

# '''

# print(course)

# index of strings in python. - similar to indexing of arrays.

# course = 'Python for Beginners'
# print(course[0:3])
# print(course[0:])
# print(course[1:])
# print(course[:5])

# # can be used to clone a string
# print(course[:])
# retuns characters from index 0 -3 but excludes the number of index 3.

# simple exercise.
# name ='Jennifer'

# print(name[1:-1])

# first_name = 'John'
# second_name = 'Philip'

# print(first_name + " [" + second_name + " ] is a coder")

# use of formatted strings to vosualize the output.
# first_name = 'John'
# second_name = 'Philip'

# message = f'{first_name}  [{second_name}] is a coder'
# print(message)

# DAY THREE 14 SEPTEMBER 2021

# course = "Pythong for Beginners"

# print(course.upper())
# print(course.lower())
# print(len(course))
# print(course.find("for"))

# # print(course.replace("for", "absolute"))

# find returns index while in retuns trythy true-false

# course = "Pythong is easy to learn"

# print("Python" in course)


# python arithmetical operations.

# print(10%3)
# print(10**3)
# print(10*3)

# x =10
# x= 10+3
# print(x)

# augmented assignmet operator.

# x=10
# x+=3
# print(x)

# x=10
# x =+3
# print(x)

# operator precedence
# exponentiation **
# mutliplication or ZeroDivision
# addition or subtraction

# x = (2+3) * 10 - 3
# print(x)

# decisions and conditions withi f statemenets.

# is_cold = True
# is_hot= True
# if is_cold:
#     print("Today is a cold day")
# elif is_hot:
#     print("IT IS HOT")
# else:
#     print("Today is a hot day")

# pratice question

# house_price = 1000000

# good_credit = True
# bad_credit = False

# d_payment = abs(house_price *0.1)
# if good_credit:
#     print(f"Downpayment is : ${d_payment}")
# elif bad_credit:
#     print(abs(house_price/20 - house_price))

# logical operators with python.

# and: both OR: at least one


# has_income = True

# had_written = False

# if has_income or had_written:
#     print("This is a good citizen")

# else:
#     print("Not an elligieble citizen")


# day four


# temperature =35

# if temperature != 30:
#     print("It is a hot day")
# else:
#     print("It is not a  hot day")

# simple challenge

# user_name = "JohnPhilipMidamba"

# if len(user_name) < 3:
#     print("Name must be at least 3 character")
# elif len(user_name) > 50:
#         print("Name can be a mazimum of 50 character")
# else:
#         print("Name looks good")


# convert either from kg to lb

# user_weight = int(input("Enter your Weight : "))

# selection = input("P for pound K for Kg : ")

# if selection == "P":
#     converted = user_weight * 0.45
#     print(f"You are {converted} kilos  of weight")
# elif selection == "k":
#         converted = user_weight / 80.45
#         print(f"You are {converted} pounds  of weight")

# Day five

# while loop to execute blocks os code mutliple times

# i = 1

# while i <=5:
#     print('*' * i)
#     i+=1
# print ('While loop is done')

# guesssing game challenge

# secret_number = 9

# guess_count = 0
# guess_limit =3


# while guess_count < guess_limit:
#     guess=int(input("Your Guess : "))
#     guess_count +=1
#     if guess == secret_number:

#         print('You Won')
#         break
# else:
#     print("You lost")

# Car game challenge

# command =''

# started = False

# while True:
#     command = input(">").lower()
#     if command == 'start':
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             print('Car has started')
#     elif command== 'stop':
#         if not started:
#             print("Car is already stopped")
#         else:
#             started= False
#             print("Car stopped")
#     elif command == 'help':
#         print('''
# Start - to start the car.
# stop - to stop the car.
# quit - Quit
#     ''')
#     elif command == 'quit':
#         break

# add numbers between 5 and 10

# num = 5
# sum = 0


# while(num < 10):
#     sum += num
#     num += 1
#     print("The result is", sum)

# multiplication table modofocation from 10 to one.

# n = 1

# user_entered = 6

# while n <= 100:
#     product = n * user_entered
#     print(n, "x", user_entered, "=", product)
#     n+=1


# DAY 6

# LEARNING OUTCOME - HOW TO USE FOR LOOPS.


# range takes three arguments (start, stop, step) - step refers to the the step ro jump to another number.

# for item in range(5,15,3):
#     print(item)

# challenge - takes an array having shopping cart items and prin the numbers in the shopping cart.

# prices=[10,20,30]
# total_price=0
# for price in prices:
#     # augmented assignment operator
#     total_price+=price
# print(f"The total price is : {total_price}")

# nested loops in python.

# for x in range(4):
#     for y in range(3):
#         print(f"{x}, {y}")
#  the first loop gets executed and jumped to the next for looper which is executed for the range provided/
# after completion, our code jumps to the initial loop and runs for the second item in the range whichi is 1.
# the process goes on untill out initial range loop is completed.

# my solution that wasnt appropriate.

# numbers =[5,2,5,2,2]

# for num in numbers:
#     for x in numbers:
#         stars ="*" * num
#         print(stars)

# best solution.

# numbers =[2,2,2,7]

# for num in numbers:
#     loop_count =''
#     for x in range(num):
#         loop_count += "x"
#     print(loop_count)

# python lists.

# solution one 
# list = [1,2,3,78,54,98,4587,68]
# larg_number = max(list)
# print(larg_number)

# solution two.
# list = [1,2,3,78,54,98,4587,68]
# large_number = list[0]

# for num in list:
#     if num >large_number:
#         large_number=num
# print(large_number)


# third solution
# list = [1,2,3,78,54,98,4587,68]
# list.sort()
# largest_num =list[-1]
# print(f"The largest number is {largest_num}")

# list =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# # print all the values in the list

# for num in list:
#     for item in num:
#         print(item)

# DAY SEVEN 7

# APPEND - Add a number on the end of the list.

# numbers =[1,2,5,4,8,78,84]

# numbers.append(20)

# print(numbers)
# will add 20 to the end of the list.
# insert - takes two parameter, index and the numbers- index specifies the index where you
#  want to add the number and the second paremeter is the number you want to add to the list.

# numbers =[1,2,5,4,8,78,84]

# numbers.insert(2,20)

# print(numbers)

# remove a number from the list provided.


# numbers=[1,2,548,85,78,96,23,69]

# numbers.remove(548)

# print(numbers)
# removes 548 from the lists

# removes all the values in the list.

# numbers=[1,2,548,85,78,96,23,69]
# numbers.clear()

# print(numbers)

# pop list method removes the last item in the list
# numbers=[1,2,548,85,78,96,23,69]
# numbers.pop()

# print(numbers)

# count() - counts the occurence of a value in the list
# numbers=[1,2,548,85,2,78,96,2,23,69]
# count = numbers.count(2)

# print(count)
# copy() - shallow copy of the original list

# numbers=[1,2,548,85,78,96,23,69]
# copy_num = numbers.copy()

# print(copy_num)

# assignment that removes tduplicates from our list.
# we can use set to remove duplicates.

# numbers=[1,2,2,548,85,78,2,96,23,69]


# rem_duplicate = list(set(numbers))

# print(rem_duplicate)

# solution 2 - Most best solution according to me.

# numbers=[1,2,548,85,78,96,23,69]

# unique_list=[]

# for number in numbers:
#     if number not in unique_list:
#         unique_list.append(number)
# print(unique_list)

# best solution according to me- well explained.


# Tuples. similarlt o lists only that we cannot mutate them- we cnnot add item to them, list them, remove, lcear or pop.
# only uses count and index.

# numbers=(1,2,548,85,78,96,23,69)
# numbers[0]=20

# print(numbers)
#     numbers[0]=20
# TypeError: 'tuple' object does not support item assignment.

# unpacking.

# numbers =(1,2,3)
# x=numbers[0]
# y=numbers[1]
# z=numbers[2]

# print(x)
# print(y)
# print(z)

# unpacking in practice.
# numbers=(1,2,3)
# x,y,z=numbers


# print(x)
# print(y)
# print(z)
# unpaclagin is not limited to tuples alone, can also be used with lists.


# Dictionaries.
# customer={

#     "name":"John Philip",
#     "age":20,
#     "birth_date":"Jan 1 1998",
#     "Town": "Eldoret"
# }

# customer["name"]="Midamba John"

# print(customer['name'])

# programm to convert number in words like is user enter 123 will return one two three
# user_input= input("Enter Phone number : ")
# number_words={
#     "0":"zero",
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four",
#     "5":"Five",
#     "6":"Six",
#     "7":"Seven",
#     "8":"Eight",
#     "9":"Nine"
# }
# output=""

# for num in user_input:
#     output += number_words.get(num, "N/A") + " "

# print(output)

# Day eight.
# Emoji convertor

# message = input("> ")

# words= message.split(' ')

# emoji={
#     ":)":"🤣",
#     ":(":"😒",

# }
# output =''
# for num in words:
#     output += emoji.get(num, num) + " "
# print(output)

# functions.
# functions in python are executed from line to line
# assignmendt starts with def which means define in python.
# declare the function first then call it.
# simple pythong fucntion implication.

# def user_message():
#     print("Hi thanks for cmiing thorugh this way")

# print("Start")
# user_message()
# print("Finished")

# parameters.

# def user_message(x):
#     print(f"Hi {x} thanks for signing up")

# print("Start")
# user_message("john")
# print("Finished")
# keyword vs positional arguments.

# always use keyword arguments after postional arguments.


# Day Nine.

# Return function return None by default incase of no return function.

# def square(x):
#     return x*x

# print(square(9))

# reusable functions.

# def emoji_convertor(message):
#     words= message.split(' ')
#     emoji={
#         ":)":"🤣",
#         ":(":"😒",

#     }
#     output =''
#     for num in words:
#         output += emoji.get(num, num) + " "
#     return output


# message = input("> ")

# print(emoji_convertor('I am sad :('))

# Exceptions - how to handle errors in programs.
# python handles erros using try except. it evaluates a given code for succes if
#  it doesnt return a succes the except block takes control.
# we can chain various errors together.

# try:
#     age= int(input('>'))
#     income=20000
#     risk=income/age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be zero')
# except ValueError:
#     print("Invalid valus/ Vale not declared")

# comments are use to add notes and comments to our programs.
# use comments to exlains whys and how not 


# Day Ten
# Classes
# we use types to define classes and classes can have methods that we define in the body of the class
# classes can also have attributes that we can set anywhre in our progrmas.
# class Point:
#     def Write(self):
#         print("Writer")
#     def draw(self):
#         print(" Draw")

# point1 = Point()

# point1.draw()


# constructs
# constrcutor is a function that get called at the time of creating an object.
# it simply creates an object.


# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def Move(self):
#         print('Move')
#     def Walk(self):
#         print("Walk")

# point = Point(10,20)
# print(point.x)

# class Person:
#     "This is a person class"
#     age = 10

#     def greet(self):
#         print('Hello')

# harry=Person()
# # Output: 10
# print(Person.age)

# # Output: <function Person.greet>
# print(Person.greet)

# # Output: "This is a person class"
# harry.greet()

# challenge

# Day  11

# class Person:
#     def Talk(self):
#         print("Talk")
#     def Name(Self):
#         print("Name")

# person1=Person()

# pjohn=person1.Name="John"
# print(pjohn)


# Inheritance, Modules, Packages.

# inheritance is used to resuse code and is not limited to python- Other languages implement it.
# it is used to avoid repetition of code and implements teh DRY method.
# class Mammal:
#     def walk(self):
#         print("Walk")

# class Dog(Mammal):
#     pass

# class Cat(Mammal):
#     pass

# dog1=Dog()
# dog1.walk()

# both dog and cat class are iheriting the walk method from the mammal class.

# Modules in python.
# modules are used to make reusable code and separate concerns inside the application
# it also impoves code readability and the sort.

# import converters

# from converters import kg_to_lbs

# tencovnet= kg_to_lbs(70)

# print(tencovnet)

# exercise challenge

# numbers =[45,1,4,8,5,9,125,458,897,120,154,7458]

# dig =0
# for num in numbers:
#     if num> dig:
#         dig=num
#         num+=1
# print(dig)

# import largestnumber

# lg_num=largestnumber.biggest_number([45,1,4,8,5,9,125,458,897,120,154,7458])

# print(lg_num)
# simple implementation of how to use a module
#  Packages are used whwen we want to organize our code together
# it also helps us avoinf bloating our code base 
# Pckages are also essential in ensuring better development practices

# import the shipping module.

# import ecommerce.shipping

# ecommerce.shipping.calculateshipping()
# from shipping is always preffered

# from ecommerce.shipping import calculateshipping

# calculateshipping()

# day 12
# build in modules in python.
# we want to use the random module in python.

# import random

# for i in range(3):
#     random.random(i)

# # class Dice with tuples that returns roll function siwh randoom values

# import random

# class Dice:
#     def roll(Self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return (first, second)
#         # alt return first , second

# dice = Dice()
# dice1 = dice.roll()
# print(dice1)
# python foles and directories.

# from pathlib import Path

# path = Path("emails")
# mkdir make directory RMDIR remove directory.
# print(path.rmdir())

# from pathlib import Path

# path = Path()

# for file in path.glob("*"):
#     print(file)

# day 13
# Pypi and Pip

# python package index
# automating tests 
# installing packages from pypi
# excel spreadshtee
#  
# automating stuffs with python package for exele openpyxl
# from openpyxl import Workbook

# wb = xl.load_workbook("transactions.xlsx")
# sheet =wb["sheet1"]
# cell = sheet['a1']
# cell =sheet.cell(1,1)

# print(sheet.max_row)

# day 15
# intro to machine learning

# underscores in python
# underscores for skipping.
# tell python to assign variable that we arent going to use anymore
# for _ in range(1,4):
#     print("Hello")

# from person import *

# p=Person()
# p.setName("Brian")
# print(f"weak private {p._name}")
# p._name="you shouldnt change this"
# print(f"weak private {p._name}")

# Double underscore
# internal use only, avoid conflict is subclass
# tells python to rewrite the name(Mangling)

# from person import Person


# p= Person()

# p.work()
# p.__think()
# Python decorators.
# everythiong in python is anobject even function can be used as objects
# decoratosa takes in a function, adds some functinality and returns it.
# 
# 


# def do_stuff(func):
#     print("Before")
#     func()
#     print("after")

# @do_stuff
# def another_thing():
#     print("Jumping on the rope")

# day 17
# Timers
