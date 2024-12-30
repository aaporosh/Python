import numpy as np

def calculate_average(scores):
    averages = np.mean(scores, axis=1)
    
    index = np.argmax(averages)
    highest_avg = averages[index]
    print(f"Student {index + 1} has the highest average score: {highest_avg:.2f}")

scores = np.array([
    [85, 90, 78],  # Student 1
    [88, 76, 92],  # Student 2
    [90, 88, 84] ])# Student 3

calculate_average(scores)
