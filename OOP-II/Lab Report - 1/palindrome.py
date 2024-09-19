def palindrome(strng) :
    return string == string[::-1]

string = str(input("String : "))
result = palindrome(string)

if  result:
    print("Yes")
else :
    print("No")