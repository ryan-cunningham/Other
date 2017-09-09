# Exercise 15 - Reading Files

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


# The textfile created for this exercise was as follows;

This is stuff I typed into a file.
It is really cool stuff.
lots and lots of fun to have in here.
