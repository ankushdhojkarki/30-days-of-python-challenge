#1. Iterate 0 to 10 using for loop, do the same using while loop.

for i in range(0,11):
    print(i)

i = 0
while i < 11:
    print(i)

    i = i + 1

#2. Iterate 10 to 0 using for loop, do the same using while loop.

for i in range (10, -1, -1):
    print(i)

i = 10
while i < 11:
    print(i)
    i = i - 1

    if i == -1:
        break

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
for i in range(7):
    print("#" * (i+1))

#4. Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
num_rows = 8
num_columns = 8

for row in range(num_rows):
    line = ""
    for col in range(num_columns):
        line += "# "
    print(line.strip())

#5. Print the following pattern:

'''0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100'''

for i in range(11):
    square = i*i
    print(f"{i} X {i} = {square}")

#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

given_list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for items in given_list:
    print(items)

#7.Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i%2 == 0:
        print(i)

#8. Use for loop to iterate from 0 to 100 and print only odd numbers

for i in range(100):
    if i%2 != 0:
        print(i)