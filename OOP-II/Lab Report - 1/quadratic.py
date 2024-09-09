#Quadratic equation : ax2+bx+c=0

import math
a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

discriminant = (b**2) - (4*a*c)
sqrt_dis = math.sqrt(abs(discriminant))
if a!=0 :
 if discriminant > 0 :
    print("Roots are real and distinct : ")
    print(f'x1 : {(-b+sqrt_dis)/(2*a)}')
    print(f'x2 : {(-b-sqrt_dis)/(2*a)}')

 elif discriminant == 0:
    print("Roots are real and equal : ")
    print(f'x : {-b/(2*a)}')

 else :
    print("Roots are imaginary :")
    print(f'x1 : {- b / (2 * a)} + i {sqrt_dis / (2 * a)}')
    print(f'x2 : {- b / (2 * a)} - i{sqrt_dis / (2 * a)}')
else:
   print("** Incorrect Input **")