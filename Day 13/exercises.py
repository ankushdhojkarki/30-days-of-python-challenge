#1. Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers =[i for i in numbers if i < 0]
print(negative_numbers)

#2. Flatten the given list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [number for sublist in list_of_lists for row in sublist for number in row]
print(flattened_list)

#3. Using list comprehension create the following list of tuples:

'''[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]'''

list_of_tuples = [(i, i**0, i**1, i**2, i**3, i**4, i**5, i**6) for i in range(11)]
print(list_of_tuples)

#4. Flatten the given list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_list = [item for sublist in countries for item in sublist]
print(new_list)

#5. Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

new_list = [{'country': c, 'city': city} for sublist in countries for c, city in sublist]
print(new_list)

#6. Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for sublist in names for first, last in sublist]
print(full_names)

#7. Write a lambda function which can solve a slope or y-intercept of linear functions.

find_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print(find_slope(1, 2, 3, 10))