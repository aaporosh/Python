student = input("Enter the list of stdent :").split()

print(len(student))
sum = 0

for n in  range(0, len(student)) :
    student[n] = int(student[n])

print(student)

for i in student :
    sum = sum + i
print(sum)