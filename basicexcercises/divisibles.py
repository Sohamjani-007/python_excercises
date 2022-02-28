# Iterate the given list of numbers and print only those numbers which are divisible by 5
l1 = [10, 20, 33, 46, 55]
for i in l1:
    if i % 5 == 0:
        print("YES", i)
    else:
        print("NO")