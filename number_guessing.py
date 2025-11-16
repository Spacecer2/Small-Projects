import random
from time import sleep

print("Welcome to the Number Guessing Game!")
sleep(1)

while True:
    true_number = random.randint(1, 10)
    print("I have chosen a number between 1 and 10.")

    while True:
        guess = input("Your guess (or 'exit' to quit): ")

        if guess.lower() == "exit":
            print("Goodbye!")
            exit()

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Enter a number between 1 and 10.")
            continue

        if not 1 <= guess <= 10:
            print("Number out of range.")
            continue

        if guess == true_number:
            print("Correct!")
            break
        else:
            print("Nope, try again.")

    if input("Play again? (yes/no): ").lower() != "yes":
        print("Goodbye!")
        break
