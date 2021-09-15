
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

