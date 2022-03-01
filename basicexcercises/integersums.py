# integersums.py
def first(n):
    num = 1
    sum = 0
    while num < n + 1:
        sum = sum + num
        num = num + 1
    return sum

def better(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum
    
def even_better(n):
    return sum(range(n + 1))


def add_it_up(n):
    try:
        result = sum(range(n + 1))
    except TypeError:
        result = 0
    return result