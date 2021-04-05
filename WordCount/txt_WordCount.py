import os
import glob


os.chdir(input("Enter a file directory: "))
txt_files = glob.glob('*.txt', recursive=True)  # Taking only txt files from the directory into a list


# creating function to read .txt files
def map_lines(file_list):
    for file in file_list:
        with open(file, "r") as fd:
            yield fd.readlines()


# Counting words..
count = 0
for line in map_lines(txt_files):
    for items in line:
        words = items.split()
        # print(words)
        for i in words:
            count += 1

print(f"{count} words counted from 'All the World's a Stage by William Shakespeare.'")


