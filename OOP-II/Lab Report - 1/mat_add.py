x = [[2,4,3],
     [1,5,3],
     [6,3,7]]

y = [[3,8,10],
     [4,9,12],
     [10,5,2]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        result[i][j] = x[i][j] + y[i][j]

for r in result :
    print(r)