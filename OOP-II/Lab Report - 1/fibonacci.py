def fibonacci(num) :
    if num <= 1 :
        return num
    else :
        return (fibonacci(num-1) + fibonacci(num-2))

num = int(input("Number : "))
print("Fibonacci Sequence : ")

for i in range(num):
    print(fibonacci(i),end=' ')