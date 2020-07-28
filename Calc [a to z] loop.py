def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


def main():
    try:
        choice = input("Enter 1,2,3 or 4: ")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except:
        print("Invalid input. Program will now terminate")

        if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))

        else:
                print("invalid input ... duh")

main()

myInstruction = input("Press Enter key to exit: ")
print(myInstruction)