start = int(input())
end = int(input())

for i in range(start,end+1):
    s = str(i)
    st = s[::-1]
    if(st == s) :
        print(s,end=' ')
