"""
You ask a user to guess a number between 1 and 50.

If they guess outside that range, you prompt with an error encouraging them to choose
a number within the proper range.

When the user eventually guesses the right number you congratulate them and
show the number of attempts they had.
"""
import random


def guess_number():

    random_num = random.randint(1,50)
    user_guess = 0
    count = 0

    while user_guess != random_num:
        user_guess = int(input("Enter a number between 1 and 50: "))
        if user_guess > 50:
            print("It is an error.. Please choose a number within the proper range!")
        elif user_guess > random_num:
            print("It is too high! Please try again..")
        elif user_guess < random_num:
            print("It is too low! Please try again..")
        count += 1

    print(f"Congratulations! You have guessed the number {user_guess} correctly after {count} attempts.")


guess_number()