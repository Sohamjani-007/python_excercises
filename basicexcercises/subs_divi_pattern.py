# Iterate the given list of numbers and print only those numbers which are divisible by 5
l1 = [10, 20, 33, 46, 55]
for i in l1:
    if i % 5 == 0:
        print("YES", i)
    else:
        print("NO")


# Write a program to find how many times substring “Emma” appears in the given string.
# Solution 1:
word_x = "Emma is good developer. Emma is a writer"
for Emma in word_x:
        print(word_x.count("Emma"))
        break


# Solution 2: Without string method # Web solution
def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    return count

count = count_emma("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")


# Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# numbers = [1, 2, 3, 4, 5]
# for items in numbers:
#     items = items + 1
for num in range(6):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")