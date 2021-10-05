# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’

# Solution 1
user = input("Write a word : ")
char = len(user)
print("Original string is ,", user)
print("Now will get only even index char")
for i in range(0, char - 1, 2):
    print("index[", i, "]", user[i])

# Solution2
# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# using list slicing
# convert string to list
# pick only even index chars
x = list(word)
for i in x[0::2]:
    print(i)
