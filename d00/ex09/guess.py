import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
print()

toFind = random.randint(1, 99)
i = 0

print(toFind)
while True:
    print("What's your guess between 1 and 99?")
    triedValue = input(">> ")
    try:
        if triedValue == "exit":
            print("Goodbye!")
            exit()
        triedValue = int(triedValue)  # catch the valueError
        if triedValue < toFind:
            print("Too low!")
        elif triedValue > toFind:
            print("Too high!")
        else:
            if toFind == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if i == 0:
                print("Congratulations! You got it on your first try")
            else:
                print("Congratulations, you've got it!")
                print("You won in", i + 1, "attempts!")
            break
    except ValueError:
        print("That's not a number.")
    i += 1
