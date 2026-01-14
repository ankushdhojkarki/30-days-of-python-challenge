#1. Write a function which generates a six digit/character random_user_id

import random, string

def random_user_id():
    chars = string.ascii_letters + string.digits
    user_id = ''
    for i in range (6):
        char = random.choice(chars)
        user_id = user_id + char
    return user_id
print(f"User ID: {random_user_id()}")

#2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

import random, string

def user_id_gen_by_user():
    char_count = int(input("Enter the number of characters: "))
    id_count = int(input("Enter the number of IDs: "))
    chars = string.ascii_letters + string.digits
    

    for i in range(id_count):
        current_id = ""
        
        for j in range(char_count):
            random_char = random.choice(chars)
            current_id = current_id + random_char

        print(current_id)
        
user_id_gen_by_user()

#3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

import random

def rgb_color_gen():
    rgb = []
    r = rgb.append(random.randint(0,255))
    g = rgb.append(random.randint(0,255))
    b = rgb.append(random.randint(0,255))
    return tuple(rgb)

print(f"rgb{rgb_color_gen()}")
