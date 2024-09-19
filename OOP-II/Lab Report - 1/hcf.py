def hcf(a,b) :
    if a>b :
        small = b
    else :
        small = a
    for i in range(1,small+1) :
        if (a%i==0) and (b%i==0):
            result = i
    return result

x = int(input("Number : "))
y = int(input("Number : "))

print(f'HCF of {x} and {y} is : {hcf(x,y)}')