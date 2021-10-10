#  Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

def reverse(num):
    rev = 0
    while(num != 0):
        reminder = num % 10
        rev = (rev * 10) + reminder
        num = num // 10
        print ("Reverse number is  : ", rev)
 
num=input("enter number : ")
reverse(int(num))

# Calculate income tax for the given income by adhering to the below rules.
# Expected Output:
# For example, suppose the taxable income is 45000 the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.

income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    x = income - 10000
    tax_payable = x * 10 / 100
else:
    tax_payable = 0
    tax_payable = 10000 * 10 / 100
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)










