def default_function():
    print("Hello! Welcome to Menu driven Program")


def add_function(x, y):
    sum = x + y
    print("the addition of 2 operand is :", sum)


def sub_function(x, y):
    sub = x - y
    print("the subtraction of 2 operand is :", sub)

if __name__ == "__main__":
    print("0. Exit")
    print("1. Default Choice")

    print("2. addition")
    print("3. subtraction")

    while True:

        choice = int(input("Enter a choice"))

        if not choice:
            break

        if choice == 1:
            default_function()

        if choice == 2:
            operand1 = int(input("enter the first operand:"))
            operand2 = int(input("enter the second operand:"))
            add_function(operand1, operand2)
        if choice == 3:
            operand1 = int(input("enter the first operand:"))
            operand2 = int(input("enter the second operand:"))
            sub_function(operand1, operand2)

        print("Thanks! Come Again")
