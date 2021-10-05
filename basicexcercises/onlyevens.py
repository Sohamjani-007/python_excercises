# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’

user = input("Write a word : ")
char = len(user)
print("Original string is ,", user)
print("Now will get only even index char")
for i in range(0, char - 1, 2):
    print("index[", i, "]", user[i])
