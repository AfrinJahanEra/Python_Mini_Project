import random

def number_guessing_game():
    number = random.randint(1, 100)
    print("Guess the number between 1 and 100")
    
    while True:
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct! You guessed the number.")
            break

number_guessing_game()
