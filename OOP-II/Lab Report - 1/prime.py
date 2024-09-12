num = int(input("Number : "))
count=False

if num>1 :
    for i in range(2,num) :
        if num%i == 0:
            count= True
            break
    if count :
        print(f'{num} is not Prime Number')
    else :
        print(f'{num} is Prime Number')

else:
     print(f'{num} is not Prime Number')