import random

letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'נ', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', '0', 'P', 'U', 'V', 'W','X','Y','Z']
numbers =['1','2','3','4','5','6','7','8','9','0'] 
symbols =['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Wellcome to password generator")

l = int(input("How many letters would you like to add : "))
n = int(input("How many number would you like to add : "))
s = int(input("How many symbols would you like to add : "))

password_list = []

for char in range(1, l+1):
    password_list.append(random.choice(letters))

for char in range(1,n+1):
    password_list.append(random.choice(numbers))

for char  in range(1,s+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
print(password_list)

password = ""

for char in password_list :
    password += char

print(password)