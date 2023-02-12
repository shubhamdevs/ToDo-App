"""
The code below is supposed to print out the items of the list with the first character of each item capitalized. However, the code contains two errors. Try to find and fix the errors.

for item in ["sandals", "glasses", "trousers"):
    print(item.capitalize)
"""

# Answer:
#   1) in the first line wrong use of brackets ")"
#   2) in the next line missing brackets for capitalize method

# Solution:
for item in ["sandals", "glasses", "trousers"]:
    print(item.capitalize())

