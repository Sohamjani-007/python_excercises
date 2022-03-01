# def my_function(str1, str2):
#     print(str1)
#     print(str2)
#
#
# my_function("This is arg1", "This is arg2 which is also a string")
# my_function("Strin7g", "Soham Jani")


## Infinite Arguments
# def print_people(*people): #(* = Infinity but not really)
#     for person in people:
#         print("This person is", person)
#
#
# print_people("Soham", "Chirag", "Rahul", "Sanjay", "Sam")
#
# check = True
#
# if check == False:
#     print("It is false")
# else:
#     print("This is True")
#FOR LOOP
# numbers = [1,2,3,4,5]
# for items in numbers:
#     print("This are some basic numbers", items)

# run = True
# current = 1
#
#
# while run:
#
#     if current == 1008000000:
#         run = False
#     else:
#         print(current)
#         current += 1


# REGEX- Regular expression:


# import re
# string = "'I AM NOT A IDIOT',but she knew she is ."
# print(string)
# new = re.sub('[A-Z]', '', string)
# print(new)
# new = re.sub('[a-z]', '', string)
# print(new)
# string = string + "2901 - 902"
# print(string)
# new = re.sub('[^0-9]', '', string)  ##**
# print(new)

#
# import re
#
#
# print("Our magical calculator")
# print("Type quit to exit\n")
#
# previous = 0
# run = True
#
#
# def performMath():
#     global run
#     global previous
#     equation = ""
#     if previous == 0:
#         equation = input("Enter equation:")
#     else:
#         equation = input(str(previous))
#
#     if equation == 'quit':
#         print("Goodbye, human.")
#         run = False
#     else:
#         equation = re.sub('[A-za-z,.:()" "]', '', equation)
#
#         if previous == 0:
#             previous = eval(equation)
#         else:
#             previous = eval(str(previous) + equation)
#
#
# while run:
#     performMath()


import os
import sys

#PEP GUIDELINES
#COMMON KNOWLEDGE OF WHITE SPACES, etc
# def my_function(one, two,
#                 three, four,
#                 five, six):
#     print("hello world")
#
#
# def second_function():
#     print("Second Function")
#
#
# my_list = [1, 2,
#            3, 4,
#            5, 6]

