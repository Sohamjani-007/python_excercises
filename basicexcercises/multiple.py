#My solution
def num():
    num1 = int(input("Put a num1 : "))
    num2 = int(input("Put a num2 : "))
    product = num1*num2
    if product < 1000:
        print(sum(product))
    else:
        print(product)

        
# Web solution
def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2

# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)

# Second condition
result = multiplication_or_sum(40, 30)
print("The result is", result)








