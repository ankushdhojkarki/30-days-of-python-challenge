#1. Write a function called is_prime, which checks if a number is prime.
 
def is_prime(n):
    if n <=1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = 29
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

#2. Write a functions which checks if all items are unique in the list.

def is_unique(n):
    if len(n) == len(set(n)):
        return True
    else:
        return False
numbers = [1,2,3,3,4,12,5]
print(f"Is Unique? {is_unique(numbers)}")

#3. Write a function which checks if all the items of the list are of the same data type.

def is_same_data_type(item):
    first_type = type(item[0])
    for i in item:
        if type(i) != first_type:
            return False
    return True
numbers = [1,2,3,0.5,'2']
print(f"Is same data type? {is_same_data_type(numbers)}")

#4. Write a function which check if provided variable is a valid python variable

import keyword

def is_valid_variable(name):
    return name.isidentifier() and not keyword.iskeyword(name)

print(f"Is valid variable name? {is_valid_variable('for')}")