# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
# My solution
previous_num = 0
for i in range(0, 11):
    sum = previous_num + i
    print("Current Num",i ,"Previous Num", previous_num,"Current num", sum )
    previous_num = i


