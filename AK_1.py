import random

def display_title():
    print("Guess the number!")

def get_limit():
    while True:
        try:
            limit = int(input("Enter the upper limit for the range of numbers: "))
            if limit >= 2:
                return limit
        except ValueError:
            pass

def play_game(limit):
    number = random.randint(1, limit)
    print(f"I'm thinking of a number from 1 to {limit}.")
    tries = 0
    while True:
        guess = int(input("Your guess: "))
        tries += 1
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"You guessed it in {tries} tries.")
            break

display_title()

while True:
    limit = get_limit()
    play_game(limit)
    again = input("Play again? (y/n): ")
    if again.lower() == "n":
        print("Bye!")
        break