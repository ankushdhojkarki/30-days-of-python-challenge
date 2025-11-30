#1. Declare an empty list
list = []

#2. Declare a list with more than 5 items
list1 = [1, 2, 'plum', 'kiwi', 5]

#3. Find the length of your list
print(len(list1))

#4. Get the first item, the middle item and the last item of the list
print(f"First Item: {list1[0]}")
print(f"Middle Item: {list1[2]}")
print(f"Last Item: {list1[-1]}")

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Ankush", "24", "6.1", "Single", "Nepal"]

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7. Print the list using print()
print(it_companies)

#8. Print the number of companies in the list
print(len(it_companies))

#9. Print the first, middle and last company
print(f"First Company: {it_companies[0]}")
print(f"Middle Company: {it_companies[len(it_companies)//2]}")
print(f"Last Company: {it_companies[-1]}")

#10. Print the list after modifying one of the companies
it_companies[0] = "Meta"
print(it_companies)

#11. Add an IT company to it_companies
it_companies.append("Adobe")
print(it_companies)

#12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, "Nvidia" )
print(it_companies)

#13.Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper()
print(it_companies) 

#14. Join the it_companies with a string '#;  '
joined_it_companies = '#: '.join(it_companies)
print(joined_it_companies)

#15. Check if a certain company exists in the it_companies list.
is_present = 'Facebook' in it_companies
print(is_present)

#16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

#17. Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

#18. Slice out the first 3 companies from the list
print(it_companies[0:3])

#19. Slice out the last 3 companies from the list
print(it_companies[-3:])

#20. Slice out the middle IT company or companies from the list
print(it_companies[len(it_companies)//2])

#21 Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

#22. Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies)//2)
print(it_companies)

#23. Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

#24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#25. Destroy the IT companies list
del it_companies
print(it_companies)

#26. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print("joined list: ", front_end)

#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5, 'python')
full_stack.insert(6, 'SQL')
print(full_stack)
