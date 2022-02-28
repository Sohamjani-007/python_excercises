# Write a program to remove characters from a string starting from zero up to n and return a new string
# my solution
name = "matplotlib"
name2 = 'machinelearning'
print(name[4::1])
# print(name2[start:stop:skip])
print(name2[3:-3:2])


# Write a function to return True if the first and last number of a given list is same. 
# If numbers are different then return False.
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
def func(numbers_list):
fnum = numbers_x[0]
lnum = numbers_y[-1]
if numbers_x == numbers_y:
    print("True")
else:
    print("False")




