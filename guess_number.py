import random

computer = random.randint(0, 20)

computer_number = computer

guess_chance = 0

print("You have 5 chances to guess my number. ")
print("Typ a number between 0-20: ")

while guess_chance < 5:
    user_number = int(input())

    if user_number == computer_number:
        print("You guessed my number")
        break
    elif user_number > computer_number:
        print("My number is smaller than yours:", user_number)
    else:
        print("My number is bigger than yours:", user_number)

    guess_chance+=1

    if not guess_chance < 5:
        print("You Lose, The number is:", computer_number)



