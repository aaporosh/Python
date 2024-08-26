s = input("Write a String \n")

s1 =[]
s2 =[]
s3 =[]

n = len(s)
for i in s :
    if i >= 'A' and i<= 'Z' :
        print(s1[i])
    if i>= 'a' and i <='z' :
        print(s2[i])
    if i >='0' and i <='9' :
        print(s3[i])
    else :
        print()

print(s,n)