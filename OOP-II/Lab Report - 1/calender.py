import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

display = calendar.month(year,month)
print(display)