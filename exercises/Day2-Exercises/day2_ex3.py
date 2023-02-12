"""
Create a program that prompts the user to input their name repeatedly. Then, the program repeatedly prints out the name with the first letter capitalized.
"""

name = input("What is your name: ")

while True:
    print(name.capitalize())
    name = input("What is your name: ")