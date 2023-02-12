"""
A programmer wrote the following program:

countries = []

while True:
    country = input("Enter the country: ")
    countries.append(country)
print(countries)
============================================
The expected output is as follows:
    Enter the country: Cambodia
    ['Cambodia']
    Enter the country: Triomindia
    ['Cambodia', 'Triomindia']
    Enter the country:

However, the code returns an error instead of the expected output. Fix the code, so it produces the expected output.
"""

# Answer: The above code has indentation error, the print function is outside the while loop. Correction:

countries = []

while True:
    country = input("Enter the country: ")
    countries.append(country)
    print(countries)
