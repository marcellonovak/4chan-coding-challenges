# Fizzbuzz Program with Python
# Marcello Novak, December 9th 2022

# Creates a fizzbuzz with user input for:
#   - Start/End values
#   - Fizz/Buzz values
#   - Fizz/Buzz words
# And checks user inputs for validity, with default values

# Get start and end values
while True:
    try:
        startInput = (int(input("Enter start of fizzbuzz (default 1): ") or "1"))
    except ValueError:
        print("Please enter a valid integer")
        continue
    else:
        break

while True:
    try:
        endInput = (int(input("Enter end of fizzbuzz (default 100): ") or "100"))
    except ValueError:
        print("Please enter a valid integer")
        continue
    else:
        break

# Get fizz and buzz values
while True:
    try:
        fizzInput = int(input("Enter value for fizz (default 3): ") or "3")
    except ValueError:
        print("Please enter a valid integer")
        continue
    else:
        break

while True:
    try:
        buzzInput = int(input("Enter value for buzz (default 5): ") or "5")
    except ValueError:
        print("Please enter a valid integer")
        continue
    else:
        break

# Get user fizz and buzz words
fizzWord = (input("Enter fizz word (default fizz): ") or "fizz")
buzzWord = (input("Enter buzz word (default buzz): ") or "buzz")

# Concatenation seemed cleanest here
for x in range(startInput, (endInput + 1)):

    # Reset output string to "XX: "
    output = (str(x) + ": ")

    # Check for fizz and buzz, concatenate
    if (x % fizzInput) == 0:
        output += fizzWord
    if (x % buzzInput) == 0:
        output += buzzWord

    # Check for neither case, output ellipses
    if ((x % fizzInput) != 0) and ((x % buzzInput) != 0):
        output += '...'
    
    print(output)
