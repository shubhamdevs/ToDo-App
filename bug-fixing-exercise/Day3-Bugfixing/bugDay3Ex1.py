"""
The programmer is trying to loop over the buttons list and print out each item with the first letter capitalized. However, the programmer has done something wrong. Try to find and fix the issue.

for i in buttons:
    print(i.capitalize())

buttons = ["cancel", "reply", "submit"]
"""
# Answer: Here the programmer assigned the list, buttons below the for loop, for python interpreter executes code line by line.

# Solution:
buttons = ["cancel", "reply", "submit"]
for i in buttons:
    print(i.capitalize())
