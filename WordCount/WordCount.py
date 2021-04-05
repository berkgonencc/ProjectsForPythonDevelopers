"""
    Ask the user what's on their mind. Then after the user responds,
count the number of words in the sentence and print that as an output.

Example:
Prompt: what's on your mind today?
Input: well, it's just a day for me to be an expert in coding
Output: oh nice, you just told me what's on your mind in 13 words!

    To take this a step further, open a file that is handed to you,
count the number of words in there, then print it out.
"""

user_input = input("What's on your mind today?\n").split()
count = 0
for i in range(len(user_input)):
    count += 1
print(f"Oh nice, you just told me what's on your mind in {count} words!")

