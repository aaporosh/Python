import time

hour = time.strftime("%H")
m = time.strftime("%M")
s =time.strftime("%S")
print(hour,m,s)

if ( int(hour) >= 6 and int(hour) <= 11):
    print("Good Morning")

elif ( int(hour) > 11 and int(hour)<=15):
    print("Good afternoon")

elif ( int(hour) >15 and int(hour) <20):
    print("Good Evening")

elif ( int(hour) >=20 and int(hour) <24 ):
    print("Good night! time to go for sleep")

else :
    print("It's mid night bro")