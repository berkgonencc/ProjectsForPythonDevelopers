"""
This is a popular game played between two people.
Each player gets to form one of three shapes using their hand:

   - rock (a closed fist)
   - paper (a flat hand)
   - scissors (a fist with the index finger and middle finger extended, forming a V)
"""

import random


# r > s, s > p, p > r
def win_condition(person, opponent):
    if (person == 'r' and opponent == 's') or (person == 's' and opponent == 'p') or (
            person == 'p' and opponent == 'r'):
        return True


def play():
    user_input = input("Enter 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user_input == computer:
        return "Tie!"

    if win_condition(user_input, computer):
        return 'You win!'

    return 'You lost!'


print(play())