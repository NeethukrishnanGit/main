#1. Write a script to declare two no's. print true if the first no is divisible by second no.print false otherwise
"""
pseudocode:
step1: declare avariable(x and y)i.e get the values from user
step2: print the variable
step3: use if else condition to perform the operation
step4:if x is divisible by y print:True, else:False
"""
x = int(input("enter x:"))
y = int(input("enter y:"))
print(x)
print(y)
if (x%y)==0:
    print("True")
else:
    print("false")
