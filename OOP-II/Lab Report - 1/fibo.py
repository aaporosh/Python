num = int(input("Number : "))

num1 = 0 
num2=1
count =0

if num==1:
    print(f'Fibonacci Sequence : {num1}')
else :
    print("Fibonacci Sequence :")
    while count < num :
        print(num1 , end=' ')
        temp = num1 + num2

        num1 = num2
        num2 = temp
        count +=1