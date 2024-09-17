# Initial Data
grades = [85, 78, 92, 45, 33, 67, 88, 41]

# a. Categorize each student's grade
print("Grade Categories:")
for score in grades:
    if score > 80:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 40:
        grade = "C"
    else:
        grade = "F"
    
    print(f"Score: {score} - Grade: {grade}")

# b. Boost grades by 5% using map() function
def boost_grades(score):
    return score * 1.05

boosted_grades = list(map(boost_grades, grades))
print("Boosted Grades:")
print(boosted_grades)

# c. Find and print boosted grades above 90 using lambda function
boosted_grades_above_90 = list(filter(lambda x: x > 90, boosted_grades))
print("Boosted Grades Above 90:")
print(boosted_grades_above_90)
