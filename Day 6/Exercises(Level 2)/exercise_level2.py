#1. Unpack siblings and parents from family_members
family_members = ("Harry", "Hermione", "James", "Lilly")
sibling1, sibling2, parent1, parent2 = family_members
print(f"Siblings: {sibling1}, {sibling2}\nParents: {parent1}, {parent2}")

#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Mango", "Kiwi", "Orange", "Avocado", "Melon", "Grapes")
vegetables= ("Potato", "Beans", "Broccoli", "Carrot", "Spinach")
animal_products = ("Milk", "Cheese", "Meat", "Butter", "Honey")
food_stuffs_tp = fruits + vegetables + animal_products
print(food_stuffs_tp)

#3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuffs_tp)
print(food_stuff_lt)

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
length = len(food_stuff_lt)
start_index = length//2-1
end_index = length//2+1
middle_slice = food_stuff_lt[start_index:end_index]
print(f"Middle Slice: {middle_slice}")

#5. Slice out the first three items and the last three items from food_staff_lt list
print(f"First 3 items: {food_stuff_lt[:3]}\nLast 3 items: {food_stuff_lt[-3:]}")

#6. Delete the food_staff_tp tuple completely
# del (food_stuffs_tp)
# print(food_stuffs_tp)

#7. Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if "Estonia" in nordic_countries:
    print(f"'Estonia' exists in Nordic Countries.")
else:
    print(f"'Estonia' does not exist in Nordic Countries.")

if "Iceland" in nordic_countries:
    print(f"'Iceland' exists in Nordic Countries.")
else:
    print(f"'Iceland' does not exist in Nordic Countries.")


