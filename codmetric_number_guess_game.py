import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Your guess is too low! Try again.")
        elif guess > secret_number:
            print("Your guess is too high! Try again.")
        else:
            print(f"Correct! You guessed the answer in {attempts} attempts.")
            break

    except ValueError:
        print("Invalid input. Please enter an integer.")
