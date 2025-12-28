#1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

def even_and_odds(number):
    even_list = []
    odd_list = []
    
    for i in range(1, number+1):
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return len(odd_list), len(even_list)

odds, evens = even_and_odds(893)
print(f"Number of odd numbers: {odds}")
print(f"Number of even numbers: {evens}")

#2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(number):
    total = 1
    for i in range(1, number+1):
        total *= i
    return total

number = 5
print(f"Factorial of {number} is {factorial(number)}")

#3. Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(item):
    if len(item)==0:
        return True
    else:
        return False

fruits = ['apple', 'kiwi', 'orange']
veggies = []
print(f"Is the fruits list empty? {is_empty(fruits)}")
print(f"Is the veggies list empty? {is_empty(veggies)}")

#4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

def calculate_mean(n):
    mean = round(sum(n)/len(n),2)
    return mean

def calculate_median(n):
    n.sort()
    length = len(n)
    mid = length//2  

    if length % 2 == 0:
        return round((n[mid-1]+n[mid])/2,2)
    else:
        return n[mid]

def calculate_mode(n):
    return max(set(n), key = n.count)

def calculate_range(n):
    return max(n) - min(n)

def calculate_variance(n):
    mu = sum(n)/len(n)
    squared_diff = sum((x-mu)**2 for x in n)
    variance = squared_diff/len(n)
    return round(variance,2)

def calculate_std(n):
    var = calculate_variance(n)
    return round(var**0.5,2)

numbers = [1,2,3,7,7,4,5,13,19,3,1,9,4,1,2,33,7,7]
print(f"Mean: {calculate_mean(numbers)}")
print(f"Median (Odd): {calculate_median(numbers)}")      
print(f"Median (Even): {calculate_median(numbers)}")
print(f"Mode: {calculate_mode(numbers)}")
print(f"Range: {calculate_range(numbers)}")
print(f"Variance: {calculate_variance(numbers)}")
print(f"Standard Deviation: {calculate_std(numbers)}")
