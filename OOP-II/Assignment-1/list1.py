customers = ["Alice", "Bob", "Charlie", "David", "Eve"]

#Access the third customer in the list and print their name
print(customers[2])

#Change the name of the second customer to "Ben".
customers[1] = "Ben"
print(customers)

#Add a new customer named "Frank" to the end of the list
customers.append("Frank")
print(customers)

#Sort the customer names alphabetically and print the final list
customers.sort()
print(customers)

#Remove the customer "David" from the list.
customers.remove("David")
print(customers)