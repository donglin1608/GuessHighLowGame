import random

def check_guess(secret_key, guess):
    if guess < secret_key:
        print("your guess is too low")
    elif guess > secret_key:
        print("your guess is too hight")
    else:
        print("you win!")