print("***Calculator***")
a=float(input("Enter the first number : "))
operator=input("Enter the oparetor : ")
b=float(input("Enter the second number : "))

if operator== "+" :
    print("The result is : ",a+b)

elif operator== "-":
    print("The result is : ",a-b)

elif operator=="*":
    print("The result is : ",a*b)

elif operator== "/":
    print("The result is : ",a/b)

elif operator== "%":
    print("The result is : ",a%b)

else :
    print("wrong input")   