li = [1, 5, 3, 6, 3, 5, 6, 1]
print("original list : " + str(li))

li2 = []
for i in li:
    if i not in li2:
        li2.append(i)

print("removing duplicates : " + str(li2))
