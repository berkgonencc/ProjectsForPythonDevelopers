"""
Welcome a user then ask them for a number between 1 and 1000.

When the user gives you the number, you check if it's odd or even and then you print a message letting them know.

Example:

Prompt: What number are you thinking?
Input: 25
Output: That's an odd number! Have another?  """

# Answer:
count = 2
while count != 0:
    user_input = int(input("What number are you thinking?\nEnter a number: "))
    count -= 1
    if user_input % 2 == 0:
        print("That's an even number!")
    else:
        print("That's an odd number!")
