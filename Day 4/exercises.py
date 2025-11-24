#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
words = ['Thirty', 'Days', 'of', 'Python']
full_str = ' '.join(words)
print(full_str)

#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
words = ['Coding', 'For', 'All']
full_str = ' '.join(words)
print(full_str)

#3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#4. Print the variable company using print().
print(company)

#5. Print the length of the company string using len() method and print().
print(len(company))

#6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

#7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9. Cut(slice) out the first word of Coding For All string.
print(company[7:])

#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
substring = "Coding"
if substring in company:
    print(f"The word '{substring}' is present.")
else:
    print(f"The word '{substring}' is not present.")

#11. Replace the word coding in the string 'Coding For All' to Python.
new_sentence = company.replace('Coding', 'Python')
print(new_sentence)

#12. Change Python for Everyone to Python for All using the replace method or other methods.
given_sentence = "Python for Everyone"
changed_to = given_sentence.replace("Everyone", "All")
print(changed_to)

#13. Split the string 'Coding For All' using space as the separator (split()) .
list_of_words = company.split(' ')
print(list_of_words)

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
given_words = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
splitted_words = given_words.split(',')
print(splitted_words)

#15. What is the character at index 0 in the string Coding For All.
character = company[0]
print(character)

#16. What is the last index of the string Coding For All.
last_char = company[-1]
print(last_char)

#17. What character is at index 10 in "Coding For All" string.
character = company[10]
print(character)

#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = "Python For Everyone"
words = phrase.split()
first_letters = [word[0].upper() for word in words]
acronym = "".join(first_letters)
print(acronym)

#19. Create an acronym or an abbreviation for the name 'Coding For All'.
phrase = "Coding For All"
words = phrase.split()
first_letters = [word[0].upper() for word in words]
acronym = "".join(first_letters)
print(acronym)

#20. Use index to determine the position of the first occurrence of C in Coding For All.
index_position = company.index('C')
print(index_position)

#21. Use index to determine the position of the first occurrence of F in Coding For All.
index_position = company.index('F')
print(index_position)

#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
index_position = company.rfind('l')
print(index_position)

#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
index_position = sentence.find('because')
print(index_position)

#24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
index_position = sentence.rindex('because')
print(index_position)

#25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sliced = sentence[31:54]
print(sliced)

#26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
index_position = sentence.find('because')
print(index_position)

#27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sliced = sentence[31:54]
print(sliced)

#28. Does ''Coding For All' start with a substring Coding?
if substring.startswith('Coding'):
    print("Yes")
else:
    print("No")

#29. Does 'Coding For All' end with a substring coding?
if company.endswith('Coding'):
    print("Yes")
else:
    print("No")

#30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
new_phrase = '   Coding For All      '  
print(new_phrase.strip(' '))

#31. Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython or thirty_days_of_python
challenge = '30Days0fPython'
print(challenge.isidentifier())
challenge1 = 'thirty_days_of_python'
print(challenge1.isidentifier())

#32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result_string = ' # '.join(libraries)
print(result_string)

#33. Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
sentence = "I am enjoying this challenge.\nI just wonder what is next."
print(sentence)

#34. Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#35. Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
output = f"The area of a circle with radius {radius} is {int(area)} meters square."
print(output)

#36. Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")