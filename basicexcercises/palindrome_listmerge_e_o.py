# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers.


# fnum = range(500)
# lnum = range(500)
# def palindrome(numbers):
#     for items in range(500):
#         if fnum == lnum:
#             print("Its a palindrome")
#             return True
#         else:
#             print("Its not a palindrome")
#             return False

def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10 # Division (floor)

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(121)
palindrome(125)


# Create a new list from a two list using the following condition

# Given a two list of numbers,
# write a program to create a new list such that the new list should contain odd numbers 
# from the first list and even numbers from the second list.
# my solution
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def result(list1,list2):
    result_list = [ ]
    for item in list1:
        if item % 2 != 0:
            result_list.append(item)      
    for num in list2:
        if item % 2 == 0:
            result_list.append(item)
    return result_list
print(result(list1,list2)

# web solution

def merge_list(list1, list2):
    result_list = []
    
    # iterate first list
    for num in list1:
        # check if current number is odd
        if num % 2 != 0:
            # add odd number to result list
            result_list.append(num)
    
    # iterate second list
    for num in list2:
        # check if current number is even
        if num % 2 == 0:
            # add even number to result list
            result_list.append(num)
    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))