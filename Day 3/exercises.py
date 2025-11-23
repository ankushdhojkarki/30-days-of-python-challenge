import math

#1. Declare your age as integer variable
my_age = 24

#2. Declare your height as a float variable
my_height = 6.1

#3. Declare a variable that store a complex number
complex_num = 5 + 3j

#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
input_base = float(input("Enter base: "))
input_height = float(input("Enter height: "))
print(f"The area of the triangle is {round(0.5 * input_base * input_height, 2)}")

#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
print(f"The perimeter of the triangle is {round(side_a + side_b + side_c, 2)}")

#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter the length: "))
width = float(input("Enter width: "))
print(f"The area of the rectangle is {round(length * width, 2)}")
print(f"The perimeter of the rectangle is {round(2 * (length + width), 2)}")

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# radius = float(input("Enter the radius: "))

print(f"The area of the circle is {round(math.pi*(radius**2),2)}")
print(f"The circumference of the circle is {round(2*math.pi*radius, 2)}")

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope

print(f"------- y = 2x - 2 -------")
print(f"Slope(m): {slope}")
print(f"Y-Intercept(c): {y_intercept} (Coordinates: (0, {y_intercept}))")
print(f"X-intercept: {x_intercept} (Coordinates: ({x_intercept}, 0))")

#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10

slope = (y2-y1)/(x2-x1)
euclidean_distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

print(f"The slope is: {slope}")
print(f"The Euclidean Distance is: {euclidean_distance} ")

#10. Compare the slopes in tasks 8 and 9.
slope_task_8 = 2
slope_task_9 = 2.0

if slope_task_8 == slope_task_9:
    print("The slope of task 8 and task 9 are equal.")
else:
    print(f"The slop of task 8 and 9 are not equal.")

#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

while True:
    x = float(input("Enter a value for x: "))

    y = ((x**2) + (6*x) + 9)
    print(f"When X = {x}, Y = {y}\n")

    if y == 0:
         break

#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.

word1 = "python"
word2 = "dragon"

if len(word1) == len(word2):
     print(f"The length of {word1} and {word2} are same.")
else:
     print(f"The lenght {word1} and {word2} are not the same.")

#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'

word1 = "python"
word2 = "dragon"

if 'on' in word1 and word2:
    print(f"'on' is found in both {word1} and {word2}.")
else:
    print(f"'on' is not found in either {word1} or {word2} or both words.")

#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence."

if 'jargon' in sentence:
    print(f"The word 'jargon' is present in the sentence. ")
else:
    print(f"The word 'jargon' is not present in the sentence. ")

#15. There is no 'on' in both dragon and python
word1 = "python"
word2 = "dragon"
statement = "There is no 'on' in both dragon and python"

if 'on' in word1 and word2:
    print(f"The statement is True.")
else:
    print(f"The statement is false.")

#16. Find the length of the text python and convert the value to float and convert it to string
word = "python"
print(f"The length of the word '{word}' is {len(word)}")
print(f"Float conversion: {float(len(word))}")
print(f"String conversion: {str(len(word))}")

#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num1 = int(input("Enter a positive number: "))

if num1 % 2 == 0:
    print(f"{num1} is an even number.")
else:
    print(f"{num1} is an odd number.")

#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
num1 = 7
num2 = 3

if (num1 // num2) == 2.7:
    print("True")
else:
    print("False")

#19. Check if type of '10' is equal to type of 10
a = '10'
b = 10

if (type(a)==type(b)):
    print("True")
else:
    print("False")

#20. Check if int('9.8') is equal to 10
a = int(float('9.8'))
b =10

if ((a)==(b)):
    print("True")
else:
    print("False")

#21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter the number of hours: "))
rate_per_hour = float(input("Enter the rate per hour: "))

print(f"Your Total Earning: {hours*rate_per_hour}")

#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
number_of_years_lived = int(input("Enter the number of years you have lived: "))
seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24
days_per_year = 365
seconds_lived = days_per_year*hours_per_day*minutes_per_hour*seconds_per_minute

print(f"You have lived for {seconds_lived} seconds.")

#23. Write a Python script that displays the following table
'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125

'''

for i in range(1, 6):
    square = i * i
    cube = i * i * i
    
    print(f"{i}\t1\t{square}\t{cube}")



