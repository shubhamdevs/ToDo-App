"""
Create a program that does the following:

1. Prompts the user to input the country they are from.

2. If the user enters the word USA, the program prints out Hello.

3. If the user enters the word  India, the program prints out Namaste.

4. If the user enters the word Germany, the program prints out Hallo.

Note: Strings are case-sensitive in Python, meaning germany and Germany are treated as two different strings.
"""
# Solutions:

country = input("Where are you form? ")

match country:
    case "USA":
        print("Hello")
    case "India":
        print("Namaste")
    case "Germany":
        print("Hallo")
