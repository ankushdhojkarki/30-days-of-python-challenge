#1. Here we have a person dictionary. Feel free to modify it!
'''        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }'''
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
person['is_married'] = person.pop('is_marred') 

print("--- Dictionary Analysis Results ---")


if 'skills' in person:
    skills_list = person['skills']
    num_skills = len(skills_list)
    
    if num_skills > 0:
        middle_index = num_skills // 2 
        middle_skill = skills_list[middle_index]
        print(f"Middle Skill: **{middle_skill}**")
    else:
        print("Middle Skill: The skills list is empty.")
else:
    print("Middle Skill: 'skills' key not found.")

if 'skills' in person:
    has_python = 'Python' in person['skills']
    print(f"Has Python Skill: **{has_python}**")
else:
    print("Has Python Skill: 'skills' key not found.")


if 'skills' in person:
    skills = person['skills']
    
   
    is_frontend = all(skill in skills for skill in ['JavaScript', 'React']) and len(skills) == 2
    is_backend = all(skill in skills for skill in ['Node', 'Python', 'MongoDB'])
    is_fullstack = all(skill in skills for skill in ['React', 'Node', 'MongoDB'])

    if is_frontend:
        title = "front end developer"
    elif is_fullstack:
        
        title = "fullstack developer"
    elif is_backend:
        title = "backend developer"
    else:
        title = "unknown title"
    
    print(f"Developer Title: **{title}**")
else:
    print("Developer Title: 'skills' key not found.")

is_married = person.get('is_married', False)
country = person.get('country')
first_name = person.get('first_name')
last_name = person.get('last_name')

if is_married and country == 'Finland':
    print(f"\nStatus: **{first_name} {last_name} lives in {country}. He is married.**")
else:
    print("\nStatus: Does not meet the criteria (not married or not living in Finland).")

print("---------------------------------")
