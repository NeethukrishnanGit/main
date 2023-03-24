def default_function():
    print("Hello! Welcome to Menu driven Program")


def add_function(x, y):
    sum = x + y
    print("the addition of 2 operand is :", sum)


def sub_function(x, y):
    sub = x - y
    print("the subtraction of 2 operand is :", sub)


def multiplication_function(x,y):
    return x * y


def div_func(x, y):
    div = x / y
    print("division is:", div)


def exponent(base, power):
    result = 1
    for i in range(power):
        result *= base
    print(result)


if __name__ == "__main__":

    print("0. Exit")



    print("1. Default Choice")

    print("2. addition")
    print("3. subtraction")
    print("4. Multiplication")
    print("5. Exponent")
    print("6 . division")

    while True:

        choice = int(input("Enter a choice"))

        if not choice:
            break

        if choice == 2:
            operand1 = int(input("enter the first operand:"))
            operand2 = int(input("enter the second operand:"))
            add_function(operand1, operand2)
        if choice == 3:
            operand1 = int(input("enter the first operand:"))
            operand2 = int(input("enter the second operand:"))
            sub_function(operand1, operand2)
        if choice == 4:
            x = int(input("Enter the number1: "))
            y = int(input("Enter the number2: "))
            print(multiplication_function())
        if choice == 5:
            base = int(input("enter the base number:"))
            power = int(input("enter the power value: "))
            exponent(base, power)
        if choice == 6:
            num1 = int(input("enter the number: "))
            num2 = int(input("enter the number: "))
            div_func(num1, num2)



        print("Thanks! Come Again")
