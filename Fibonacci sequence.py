print("Program the Fibonacci sequence up to n-th term where n provided by the user")

nterms = int(input("How many terms? "))
nterms = 10
n1 = 0
n2 = 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence upto",nterms,":")
    while count < nterms:
        print(n1, end=' , ')
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

myInstruction = input("Press Enter key to exit: ")
print(myInstruction)

# Program to display the Fibonacci sequence up to n-th term where n is provided by the user
# https://www.programiz.com/python-programming/examples/fibonacci-sequence
# change this value for a different result
# first two terms
