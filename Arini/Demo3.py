def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("choose one option:")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
x=input("enter option: ")
num1=int(input("enter number: "))
num2=int(input("enter number: "))
if x=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif x=='2':
    print(num1,"-",num2,"=",sub(num1,num2))
elif x=='3':
    print(num1,"*",num2,"=",mul(num1,num2))

elif x=='4':
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("invalid option")

