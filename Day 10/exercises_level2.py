#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
total_sum = 0
for i in range(101):
    total_sum +=  i
print(f"The sum of all numbers is: {total_sum}")

#2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

# The sum of all evens is 2550. And the sum of all odds is 2500.
total_even_sum = 0
total_odd_sum = 0

for i in range(101):
    if i%2 == 0:
        total_even_sum += i
    
    else:
        total_odd_sum += i

print(f"The sum of all even numbers: {total_even_sum}")
print(f"The sum of all odd numbers: {total_odd_sum}")