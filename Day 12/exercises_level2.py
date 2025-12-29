#1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random

def list_of_hexa_colors(count):
    chars = "0123456789abcdef"
    list_of_colors = []

    for i in range(count):
        new_color = "#"

        for j in range(6):
            new_color = new_color + random.choice(chars)
    
        list_of_colors.append(new_color)
        
    return list_of_colors

print(list_of_hexa_colors(3))

#2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

import random, string

def list_of_rgb_colors(count):
    all_colors = []
    for i in range(count):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color_string = f"rgb({r},{g},{b})"
        all_colors.append(color_string)
    return all_colors

print(f"rgb color: {list_of_rgb_colors(5)}")

#3. Write a function generate_colors which can generate any number of hexa or rgb colors.
import random, string

def generate_colors(color_choice, count):
    hexa_colors = []
    rgb_colors = []
    chars = "0123456789abcdef"

    if color_choice == "hex":

        for i in range(count):
            new_color = "#"
            for j in range(6):
                new_color = new_color + random.choice(chars)
            hexa_colors.append(new_color)
        return hexa_colors
    
    elif color_choice == "rgb":
            for k in range(count):
                r = random.randint(0,255)
                g = random.randint(0,255)
                b = random.randint(0,255)
                color_string = f"rgb({r},{g},{b})"
                rgb_colors.append(color_string)
            return rgb_colors
    else:
        return "Invalid choice! Please choose either 'hex' or 'rgb'."

color_choice = input("Type 'hex' for hex colors and 'rgb' for rgb colors: ").lower()
count = int(input("Enter the number of colors you want to generate: "))
print(f"{color_choice} color: {generate_colors(color_choice, count)}")

