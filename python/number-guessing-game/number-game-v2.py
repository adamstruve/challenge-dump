import random

# The random number
number = random.randint(1, 100)

# The number of guesses
guesses = 10

# The number of guesses the user has made
guesses_made = 0

def get_input(message):
    while True:
        try:
            guess = int(input(f"{message} "))
            check_guess(number, guess)
            break
        except:
            print("That's not a valid option!")

def check_guess(number, guess):
    global guesses_made
    guesses_made += 1
    if (guess < 1 or guess > 100):
        message = "Don't waste guesses! The number is between 1 and 100:"
        get_input(message)
    elif guesses == guesses_made:
        print(f"You used all {guesses} of your guesses! The number was {number}.")
    elif guess < number:
        message = f"Too low! You have {guesses - guesses_made} guesses left. Guess again:"
        get_input(message)
    elif guess > number:
        message = f"Too high! You have {guesses - guesses_made} guesses left. Guess again:"
        get_input(message)
    else:
        print(f"Yes! It was {number}! You guessed it in {guesses_made} tries!")

def start_game():
    message = f"You have {guesses} tries to guess the number between 1 and 100:"
    get_input(message)

start_game()




