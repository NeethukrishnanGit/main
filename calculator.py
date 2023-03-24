operand1=int(input("enter the first operand"))
operation=input("+ for additin, - for subtraction, * for multiplication, / for division \n enter your choice:")
operand2=int(input("enter the second operand"))
if operation =="+":
    print("the sum is", operand1+operand2)
elif operation =="-":
    print("the difference is", operand1-operand2)
elif operation =="*":
    print("the multiplication is", operand1*operand2)
elif operation =="/":
    print("the division is", operand1/operand2)
else:
    print("your choice is invalid \n please enter the correct option")