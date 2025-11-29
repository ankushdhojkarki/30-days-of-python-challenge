#1. Write a code which gives grade to students according to theirs scores:

'''80-100, A
70-89, B
60-69, C
50-59, D
0-49, F'''

score = int(input("Enter your Score: "))

if score >= 0 and score <= 49:
    print(f"Your Grade is 'F'")

elif score>= 50 and score <= 59:
    print(f"Your Grade is 'D'")

elif score >= 60 and score <= 69:
    print(f"Your Grade is 'C'")

elif score >= 70 and score <= 89:
    print(f"Your Grade is 'B'")

elif score >= 80 and score <=100:
    print(f"Your Grade is 'A'")

#2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']

month = input("Enter the month: ")

if month.title() in autumn:
    print(f"The Season is Autumn.")
    
elif month.title() in winter:
    print(f"The Season is Winter.")

elif month.title() in spring:
    print(f"The Season is Spring.")

elif month.title() in summer:
    print(f"The Season is Summer.")

else:
    print(f"Invalid Month!")

#3. The following list contains some fruits:
'''fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')'''

fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = input("Enter a fruit name to check and add: ").lower()

if new_fruit in fruits:
    print(f"'{new_fruit.title()}' already exists in the list.")

else:
    fruits.append(new_fruit)
    print(f"'{new_fruit.title()}' added to the list.")
    print("Modified list:", fruits)


