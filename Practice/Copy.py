import numpy as np
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
row = data[0, :]
column = data[:, 1].copy()
print("Original data:")
print(data)
row[0] = 99  
column[0] = 999  
print("\nAfter modifying the row:")
print("View:", row)
print("Original data:\n", data)
print("\nAfter modifying the copy column:")
print("Copy:", column)
print("Original data:\n", data)
