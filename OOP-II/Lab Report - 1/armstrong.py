num = input("Number : ")

length =  len(str(num))
sum =0 
n = int(num)
while n > 0:
    digit =n %10
    sum+= digit**length
    n //= 10

if n == sum :
    print(f'{num} is Armstrong Number')
else:
    print(f'{num} is not Armstrong Number')