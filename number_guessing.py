import random
from time import sleep

print("Welcome to the Number Guessing Game!")
sleep(1)

run = True

while run == True:

    guessed_number = int(input(f"Guess a number between 1 and 10.: "))

    true_number = random.randint(1, 10)

    if guessed_number == true_number:
        print("You guessed correctly!")
    else:
        print(f"Sorry, the correct number was {true_number}.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        run = False

print("Thanks for playing! Goodbye!")