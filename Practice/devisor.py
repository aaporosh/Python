try:
    values = [10, 20, 30, 0]
    divisor = int(input("Enter a number:"))
    for i in values:
        result = i/divisor
        print(result)
except ZeroDivisionError:
    print("Value divided by zero")
except ValueError:
    print("Value error")
except TypeError:
    print("Type error")


