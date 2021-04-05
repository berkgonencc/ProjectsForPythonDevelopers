"""
Ask the user to give you three words. Then check if any of the five words is a palindrome.

A palindrome is a word that remains the same whether it's read forward or backward.

Example:
- madam is a palindrome.
- so is malayalam.
- But not geeks.
"""

user_input1 = input("Enter a word to check palindrome: ")
user_input2 = input("Enter a word to check palindrome: ")
user_input3 = input("Enter a word to check palindrome: ")


def palindrome(my_str):
    return my_str[::-1]


if palindrome(user_input1) == user_input1:
    print(f"{user_input1} is a palindrome")
elif palindrome(user_input2) == user_input2:
    print(f"{user_input2} is a palindrome")
elif palindrome(user_input3) == user_input3:
    print(f"{user_input3} is a palindrome.")