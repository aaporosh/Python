course = {
    "CSE101" : { "Course name" : "Introduction to Programming",
            "Credits": 3,
            "Instructor": "Dr. Alice"},
    "CSE102"  : {"Course name" : "Data Structures",
                 " Credits" : 4, 
                 "Instructor" : "Dr. Bob"},
    "CSE103" : { "Course name" : "Database Systems",
                " Credits" : 3, 
                "Instructor" : "Dr.Carol"}

}
print(course)

#Update Instructor's name

course["CSE102"]['Instructor'] = "Dr. Bob Jr."
print()
print("After changing Instructor's Name : ")
print(course)

#Add a new course :

course['CSE104'] = {'Course name ': "Algorithms",
                     'Credits' : 4,
                   'Instructor ': "Dr. Dave"}

print()
print("After Adding new course : ")
print(course)

#Loop through the dictionary and print the course code along with its details
print()
for i in course :
    print(i , course[i])

#Remove the course CSE101 from the dictionary :

course.pop('CSE101')
print()
print("After removing CSE101 course : ")
print(course)