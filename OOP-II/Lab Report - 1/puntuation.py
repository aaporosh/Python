str = input("String : ")

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for i in str:
    if i in punc:
        str = str.replace(i, "")

print("Result : ",str)
