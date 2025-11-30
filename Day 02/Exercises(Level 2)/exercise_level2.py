import math

first_name = "Ankush"
last_name = "Karki"
full_name = "Ankush Karki"
country = "Nepal"
city = 'Kathmandu'
age = 24
is_married = 'No'
is_true = "Yes"
is_light_on = "No"
programming_language, ide = "python", "VS Code"
num_one = 5
num_two = 4
total = (num_one + num_two)
diff = (num_two - num_one)
product = (num_one * num_two)
division = (num_one / num_two)
remainder = (num_two % num_one)
exp = (num_one ** num_two)
floor_division = (num_one // num_two)
radius = int(input("Enter the radius: "))
area_of_circle = (math.pi * (radius ** 2))
circum_of_circle = (2 * math.pi * radius)

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(programming_language))
print(type(ide))
print(len(first_name))
print(len(last_name))
print(round(area_of_circle, 2))
print(round(circum_of_circle, 2))


if len(first_name) == len(last_name):
    print(f"The length of your first name and last name are equal.")
else:
    print(f"The length of your first name and last name are not equal.")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter which country you are from: ")
age = int(input("Enter your age: "))


