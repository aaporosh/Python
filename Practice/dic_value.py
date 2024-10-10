subject_scores = {'Math': [90, 85, 88, 92, 95],
                  'Physics': [75, 80, 85, 90, 95],
                  'Chemistry': [85, 90, 92, 88, 82]}

avg = {}

for subject,score in subject_scores.items():
    average = sum(score)/len(score)
    avg[subject] =  average

print(avg)


student = [1,2,3,4,5,6]
status = ['yes','no','yes','no','yes','yes']

info = {}

info = dict(zip(student,status))
print(info)
updated = []
for stu,sta in info.items():
    if sta == 'yes' :
        updated.append(stu)

print(updated)


movies = {
    "The Shawshank Redemption": ["drama"],
    "The Godfather": ["crime", "drama"],
    "The Dark Knight": ["action", "crime", "thriller"],
    "Fight Club": ["drama", "thriller"]
}
l = []
for name,author in movies.items() :
    if  "action" in author or "thriller" in author :
        l.append(name)
print(l)

