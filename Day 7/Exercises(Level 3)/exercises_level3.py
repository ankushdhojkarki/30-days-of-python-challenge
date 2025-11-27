age = [22, 19, 24, 25, 26, 24, 25, 24]

#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
length_age = len(age)
set_age = set(age)
length__set_age = len(set_age)
print(f"Length of the list of age : {length_age}")
print(f"Length of the set of age: {length__set_age}")

if length_age > length__set_age:
    print("Length of the list of age is bigger.")
else:
    print("Length of the set of age is bigger.")

#2. Explain the difference between the following data types: string, list, tuple and set
'''
STRING:
*Mutability: Immutable
*Order: Ordered
*Duplicates: Allowed

LIST:
*Mutability: Mutable
*Order: Ordered
*Duplicates: Allowed

TUPLE
*Mutability: Immutable
*Order: Ordered
*Duplicates: Allowed

SET
*Mutability: Imutable
*Order: Unordered
*Duplicates: Not Allowed

'''

#3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words."

cleaned_sentence = sentence.lower().replace('.', '')
word_list = cleaned_sentence.split()
unique_words = set(word_list)
unique_word_count = len(unique_words)

print(f"List of all words (including duplicates): {word_list}")
print(f"Set of unique words: {unique_words}")
print(f"The number of unique words is: {unique_word_count}")