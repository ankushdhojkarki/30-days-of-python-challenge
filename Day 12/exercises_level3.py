#1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list(any_list):
    random.shuffle(any_list)
    return any_list

fruits = ["mango", "apple", "guava"]
print(f"Original list: {fruits}")
print(f"Shuffles list: {shuffle_list(fruits)}")

#2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
import random

def seven_unique_num():
    return random.sample(range(10),7)

print(seven_unique_num())