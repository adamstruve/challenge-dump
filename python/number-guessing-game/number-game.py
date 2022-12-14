import random

# The number of guesses
guesses = 10

# The number of guesses the user has made
guesses_made = 0

def check_guess(number, guess):
    global guesses_made
    guesses_made += 1
    if guesses == guesses_made:
        print(f"You used all {guesses} of your guesses! The number was {number}.")
    elif guess < number:
        guess = int(input(f"Too low! You have {guesses - guesses_made} guesses left. Guess again:"))
        check_guess(number, guess)
    elif guess > number:
        guess = int(input(f"Too high! You have {guesses - guesses_made} guesses left. Guess again:"))
        check_guess(number, guess)
    else:
        print(f"You guessed the number in {guesses_made} tries!")

def start_game():
    # The random number
    number = random.randint(1, 100)
    guess = int(input(f"You have {guesses} tries to guess the number between 1 and 100: "))
    check_guess(number, guess)

start_game()
