import math

'''
1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

2. Find an Euclidian distance between (2, 3) and (10, 8)

'''

print(type(23))
print(type(2.3))
print(type(4 - 4j))
print(type('This is a sting.'))
print(type(True))
print(type(['mango', 'orange', 'kiwi', 'melon']))
print(type((28.3949, 84.1240)))
print(type({1, 8, 'ram', 'lalitpur', 'pizza'}))
print(type({'name':'Gita', 'age':20, 'sex':'female', 'city': 'kathmandu'}))


#Euclidian Distance

Xa = int(input('Enter the value for Xa: '))
Xb = int(input('Enter the value for Xb: '))
Ya = int(input('Enter the value for Ya: '))
Yb = int(input('Einter the value for Yb: '))

c = round(math.sqrt(((Xa - Xb)**2) + ((Ya - Yb)** 2)), 2)

print(f"\nThe Euclidian distance between the user entered values is : {c}")