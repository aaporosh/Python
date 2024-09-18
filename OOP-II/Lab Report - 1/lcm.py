import math
def lcm(num1,num2)  :
    gcd = math.gcd(num1,num2)
    l = (num1*num2)//gcd
    return l

num1 = int(input())
num2 = int(input())
result = lcm(num1,num2)

print(f'LCM of two number : {result}')