sentence = "Learning Python is fun and rewarding."

#Extract the substring "Python is fun" using negative slicing.
print(sentence[-28:-15])

#Modify the original string by replacing "rewarding" with "exciting".
print(sentence.replace("rewarding" , "exciting"))

#Insert the phrase " Keep practicing!" after "exciting" in the modified string without directly
#concatenating it to the end. Instead, insert it at the correct position programmatically.

length = len(sentence)
phrase = " Keep practicing!"

print(sentence[:length]+phrase)

#Capitalize the first letter of each word in the final output.

print(sentence.title())