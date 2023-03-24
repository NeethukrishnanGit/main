#minicalculator
def addition():
    return x+y
def subtraction():
    return x-y
def multiplication():
    return x*y
def division():
    return x/y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
p=input("Enter your choice: ")
x=int(input("Enter the number1: "))
y=int(input("Enter the number2: "))
if p=="1":
    print(addition())
elif p=="2":
    print(subtraction())
elif p=="3":
    print(multiplication())
elif p=="4":
    print(division())

