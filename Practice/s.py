import re
def characters(input):
    capital = ''.join([char for char in input if char.isupper()])
    small= ''.join([char for char in input if char.islower()])
    integers = ''.join(re.findall(r'\b\d+\b', input))
    symbols = ''.join([char for char in input if not char.isalnum()])

    print("Capital Letters:", capital)
    print("Small Letters:", small)
    print("Integers:", integers)
    print("Symbols:", symbols)

# Get user input
input = input("Enter a string: ")
characters(input)