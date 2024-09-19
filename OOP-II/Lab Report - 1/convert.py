def binary(num):
    if num == 0:
        return ""
    result = binary(num // 2)
    return result + str(num % 2)

def octal(num):
    if num == 0:
        return ""
    result = octal(num // 8)
    return result + str(num % 8)

def hexa(num):
    if num == 0:
        return ""
    result = hexa(num // 16)
    hex_digit = num % 16
    if hex_digit < 10:
        return result + str(hex_digit)
    else:
        return result + chr(ord('A') + hex_digit - 10)

num = int(input("Number: "))

if num == 0:
    print(f'Binary: 0\nOctal: 0\nHexadecimal: 0')
else:
    b = binary(num)
    o = octal(num)
    h = hexa(num)
    print(f'Binary: {b}\nOctal: {o}\nHexadecimal: {h}')
