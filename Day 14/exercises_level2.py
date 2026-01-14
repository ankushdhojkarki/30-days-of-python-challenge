#1. Use map to create a new list by changing each country to uppercase in the countries list
countries = ["Estonia", "Finland", "Sweden", "Denmark"]

def change_to_upper(country):
    return country.upper()

countries_upper_case = list(map(change_to_upper, countries))
print(countries_upper_case)

#2. Use map to create a new list by changing each number to its square in the numbers list
numbers = [1, 2, 3, 4, 5]

def square(n):
    return n ** 2

numbers_squared = list(map(square, numbers))
print(numbers_squared)

#3. Use map to change each name to uppercase in the names list
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]

def make_uppercase(name):
    return name.upper()

names_upper_case = list(map(make_uppercase, names))

print(names_upper_case)

#4. Use filter to filter out countries containing 'land'.
countries = ["Estonia", "Finland", "Sweden", "Denmark"]

def has_land(country):
    return "land" in country.lower()

land_countries = list(filter(has_land, countries))

print(land_countries)

#5. Use filter to filter out countries having exactly six characters.
countries = ["Estonia", "Finland", "Sweden", "Denmark"]

def has_six_chars(country):
    return len(country) == 6
six_char_countries = list(filter(has_six_chars, countries))

print(six_char_countries)

#6. Use filter to filter out countries containing six letters and more in the country list.
countries = ["Estonia", "Finland", "Sweden", "Denmark"]
def six_or_more_letters(country):
    return len(country) >= 6

long_countries = list(filter(six_or_more_letters, countries))

print(long_countries)


#7. Use filter to filter out countries starting with an 'E'
countries = ["Estonia", "Finland", "Sweden", "Denmark"]

def starts_with_e(country):
    return country.startswith('E')

e_countries = list(filter(starts_with_e, countries))

print(e_countries)

#8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce
processed_list = [n**2 for n in numbers if n**2 > 10]
final_sum = reduce(lambda a, b: a + b, processed_list)

print(final_sum)

#9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):

    def is_string(item):
        return isinstance(item, str)

    return list(filter(is_string, lst))
mixed_list = ["Python", 100, "Java", True, "C++", 3.14]
strings_only = get_string_lists(mixed_list)

print(strings_only)

#10. Use reduce to sum all the numbers in the numbers list.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
def add_numbers(a, b):
    return a + b
total_sum = reduce(add_numbers, numbers)
print(total_sum)

#11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
from functools import reduce

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
def concatenate_countries(accumulator, country):
    if country == countries[-1]:
        return f"{accumulator}, and {country}"
    return f"{accumulator}, {country}"
sentence_start = reduce(concatenate_countries, countries)
full_sentence = f"{sentence_start} are north European countries"

print(full_sentence)

#12. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Estonia", 
    "Finland", "Iceland", "Ireland", "Kazakhstan", "Pakistan", "Thailand"
]

def categorize_countries(country_list, pattern):
    def matches_pattern(country):
        return pattern.lower() in country.lower()
    return list(filter(matches_pattern, country_list))

land_countries = categorize_countries(countries, 'land')
stan_countries = categorize_countries(countries, 'stan')
ia_countries = categorize_countries(countries, 'ia')

print(f"Land countries: {land_countries}")
print(f"Stan countries: {stan_countries}")
print(f"IA countries: {ia_countries}")

#13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", 
    "Brazil", "Belgium", "Canada", "Denmark", "Estonia", 
    "Finland", "France", "Germany", "Iceland"
]

def count_starting_letters(country_list):
    counts = {}
    
    for country in country_list:
        first_letter = country[0].upper()
        if first_letter in counts:
            counts[first_letter] += 1
        else:
            counts[first_letter] = 1
            
    return counts
result = count_starting_letters(countries)
print(result)

#14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# Sample list representing the data structure in the countries.js/data folder
countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", 
    "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", 
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados"
]

def get_first_ten_countries(country_list):

    return country_list[:10]
first_ten = get_first_ten_countries(countries)
print(first_ten)

#15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", 
    "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", 
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados",
    "Belarus", "Belgium", "Belize", "Benin", "Bhutan"
]

def get_last_ten_countries(country_list):
    return country_list[-10:]
last_ten = get_last_ten_countries(countries)
print(last_ten)





