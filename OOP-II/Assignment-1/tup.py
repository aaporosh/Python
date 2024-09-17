books = (
("To Kill a Mockingbird", "Harper Lee", 1960),
("1984", "George Orwell", 1949),
("The Great Gatsby", "F. Scott Fitzgerald", 1925)
)

tags = {"classic", "dystopian", "novel", "literature"}

#Access the second book's author and print it
author = books[1][1]
print(f"Author of the second book : {author}")

#Add a new record to the books tuple
new_book = ("Brave New World", "Aldous Huxley", 1932)
books = books + (new_book,)
print("Updated tuple:")
print(f'{books}\n')
      
#Unpack the details of the third book into separate variables and print them
title, author, year = books[2]
print(f" Title: {title},\n Author: {author},\n Year: {year}\n")

#Loop through the books tuple and print each book's title.
print("Title of the Books : ")
for title in books:
    print (title[0]) 

#Add a new tag "sci-fi" to the tags set and print the updated set.
print(f'\nSet Items : \n')
tags.add("sci-fi")
print(tags)

#Use a method to remove the tag "novel" from the tags set and print the updated set.
tags.remove("novel")
print("\nAfter remove : ")
print(tags)