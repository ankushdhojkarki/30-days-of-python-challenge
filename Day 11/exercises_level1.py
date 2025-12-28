#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(1,2))

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

import math
def area_circle(r):
    area = round(math.pi*r*r,2)
    return area
print(f"Area of circle: {area_circle(2)}")

#3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*args):
    total = 0
    for i in args:
        if isinstance(i, (int, float)):
         total+=i
        else:
            return("Error: Only numbers are accepted")
    return total
print(f"Total: {add_all_nums(1,2,3,4,5)}")
print(f"Total: {add_all_nums(1,2,3,4,5, 'a')}")
print(f"Total: {add_all_nums(1,2,3,4,5,9)}")

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def celsius_to_fahrenheit(temp):
    conversion = round((temp*(9/5)+32),2)
    return conversion
print(f"Celsius to Fahrenheit: {celsius_to_fahrenheit(17)}")
    
#5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):

    autumn = ['september', 'october', 'november']
    winter = ['december', 'january', 'february']
    spring = ['march', 'april', 'may']
    summer = ['june', 'july', 'august']

    if month in autumn:
        return "autumn"
    elif month in winter:
        return "winter"
    elif month in spring:
        return "spring"
    elif month in summer:
        return "summer"
    else:
        return ("Enter a valid month")

month = input("Enter a month: ").lower()    
print(f"It's {check_season(month)} season during the month of {month}.")

#6. Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, x2, y1, y2):
    m = round((y2-y1)/(x2-x1),2)
    return m
print(f"Slope: {calculate_slope(x1=2,x2=3,y1=8,y2=6)}")

#7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

import math
def solve_quadratic_eqn(a,b,c):
    d = (b**2) - (4*a*c)

    if d<0:
        return "No real solution"
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return x1, x2

print(f"Solution set of quadratic equation: {solve_quadratic_eqn(a=1, b =-5, c=6)}")

# #8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(fruit):

    for items in fruit:
        print(items)
    
fruits = ['apple', 'melon', 'kiwi', 'pineapple', 'guava']
    
print(print_list(fruits))

#9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(item):
    new_list = []
    for i in item:
        new_list.insert(0, i)
    return new_list
my_list = [1,2,3,4,5]

print(f"Original List: {my_list}")
print(f"Reversed list: {reverse_list(my_list)}")

#10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(lowercase_list):
    capitalized_list = []

    for i in lowercase_list:
        capitalized_list.append(i.upper())
    return capitalized_list

lowercase_list = ['apple', 'ball', 'ink']
print(f"Capitalized: {capitalize_list_items(lowercase_list)}")

#11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(veggies, new_item):
    veggies_list.append(new_item)
    return veggies_list
veggies_list = ['carrot', 'potato', 'spinach', 'radish', 'peas']
print(f"Appended list: {add_item(veggies_list, 'kiwi')}")

#12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(veggies, new_item):
    veggies.remove(new_item)
    return veggies_list
veggies_list = ['carrot', 'potato', 'spinach', 'radish', 'peas']
print(f"Original List: {veggies_list}")
print(f"Removed List: {remove_item(veggies_list, 'peas')}")

#13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(nums):
    total = 0
    for num in range(1, nums+1):
        total+=num
    return total
print(f"Sum of all numbers: {sum_of_numbers(10)}")

#14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(n):
    total = 0
    for num in range (1, n+1):
        if num % 2 != 0:
            total+=num
    return total
print(f"Sum of odd numbers: {sum_of_odds(10)}")

#15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(n):
    total = 0
    for num in range(1, n+1):
        if num % 2 == 0:
            total+=num
    return total
print(f"Sum of all even numbers: {sum_of_even(10)}")



