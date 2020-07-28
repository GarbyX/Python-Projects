# Python program to find the largest number among the three input numbers
# change the values of num1, num2 and num3
# for a different result
# uncomment following lines to take three numbers from user

print("This is a simple program that finds the largest number among three input numbers")
print("Created by Gabriel")

myName = input("Enter Name: ")
print(myName)
myVar = "Hello and welcome to the World of Computer Programming"
print(myVar)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("The largest number between num1, num2 and num3 is largest")


myInstruction = input("Press Enter key to exit: ")\

print(myInstruction)
