def default_function():
    print("Hello! Welcome to Menu driven Program")


def add_function(x, y):
    sum = x + y
    print("the addition of 2 operand is :", sum)


if __name__ == "__main__":
    print("0. Exit")
    print("1. Default Choice")

    print("2. addition")

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

    print("Thanks! Come Again")
