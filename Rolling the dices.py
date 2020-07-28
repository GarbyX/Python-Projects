import random
min = 1
max = 6

roll_again = "yes"

while not (roll_again != "yes" and not (roll_again == "y")):
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(min, max))
    print(random.randint(min, max))
    roll_again = input("Roll the dices again?")


myInstruction = input("Press Enter key to exit: ")
print(myInstruction)
