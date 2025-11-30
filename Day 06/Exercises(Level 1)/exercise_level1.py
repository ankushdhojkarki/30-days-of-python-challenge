#1. Create an empty tuple
empty_tuple = ()

#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brother = ("Harry",)
sister = ("Hermione",)

#3. Join brothers and sisters tuples and assign it to siblings
siblings = brother + sister
print(f"siblings: {siblings}")

#4. How many siblings do you have?
print(f"Number of siblings: {len(siblings)}")

#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_list = list(siblings)

family_list.append("James")
family_list.append("Lilly")

family_members = tuple(family_list)
print(f"Family members: {family_members}")