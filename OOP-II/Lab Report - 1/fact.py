def factorial(num) :
    if num == 1 or num == 0 :
        return 1
    else :
        return (num*factorial(num-1))

num = int(input("Number : "))
result = factorial(num)
print(f'Factorial of {num} is : {result}')