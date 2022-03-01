# solution1
def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data = [alpha[i] 
    for i in range(n):
        items = list(range(n))
        items = items[:-1]+items[::-1]
        for i in items:
            temp = data[-(i+1):]
            row = temp[::-1]+temp[1:]
            print("-".join(row).center(n*4-3, "-"))

def print_rangoli(n):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data = [alpha[i] for i in range(n)]
    items = list(range(n))
    items = items[:-1]+items[::-1]
    for i in items:
        temp = data[-(i+1):]
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(n*4-3, "-"))

n = int(input())
print_rangoli(n)

#solution2
def print_rangoli(size):
    myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    
    for i in range(size-1, -size, -1):
        x = abs(i)
        if x >= 0:
            line = myStr[size:x:-1]+myStr[x:size]
            print ("--"*x+ '-'.join(line)+"--"*x)