year = int(input("Year : "))

if year%400==0 and year%200==0 :
    print(f'{year} Year is Leap Year')
elif year%4==0 and year%100!=0:
    print(f'{year} Year is Leap Year')
else  :
    print(f'{year} Year is not Leap Year')