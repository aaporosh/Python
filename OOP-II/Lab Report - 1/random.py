import string
import random

num = (input("Length of random string: "))

# Generate random string
res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=num))

print(f"Generated random string: {res}")
