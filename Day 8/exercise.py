#1. Create an empty dictionary called dog
dog = {}

#2. Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'Pepper', 'color':'brown', 'breed':'Husky', 'legs':4, 'age':1}
print(dog)

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name':'John', 'last_name':'Sanchez', 'gender':'Male', 'marital_status':'Single', 'skills':['Python', 'Django', 'GitHub', 'DRF', 'REST API'], 'country':'Tuvalu', 'address': '36th street'}

#4. Get the length of the student dictionary
print(len(student))

#5. Get the value of skills and check the data type, it should be a list
print(student.get('skills'))

#6. Modify the skills values by adding one or two skills
student['skills'] += ['HTML, CSS']

#7. Get the dictionary keys as a list
print(list(student.keys()))

#8. Get the dictionary values as a list
print(list(student.values()))

#9. Change the dictionary to a list of tuples using items() method
print(student.items())

#10. Delete one of the items in the dictionary
student.pop('address')
print(student)

#11. Delete one of the dictionaries
del dog
print(dog)
