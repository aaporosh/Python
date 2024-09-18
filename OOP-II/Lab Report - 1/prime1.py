def prime(start,end):
    l =[]
    count = 0

    for i in range(start,end):
        for j in range(2,i):
            if (i%j ==  0):
                count  = 1
                break
            else  :
                count = 0
        if  count==0:
            l.append(i)
    return l

start  = int(input("Starting Number : "))
end = int(input("Ending Number : "))

num = prime(start,end)

if len(num)==0:
    print("Empty")
else :
    print(f'Prime numbers list :\n{num}')