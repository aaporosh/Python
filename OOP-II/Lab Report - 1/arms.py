start , end = input().split()
s = int(start)
e = int(end)

for i in range(s , e+1):
    length =  len(str(i))
    sum =0 
    n = int(i)
    while n > 0:
        digit =n %10
        sum+= digit**length
        n //= 10
    
    if i == sum :
        print(i,end=' ')
