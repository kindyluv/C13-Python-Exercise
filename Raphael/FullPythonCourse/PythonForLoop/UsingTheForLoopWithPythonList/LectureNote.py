# # ### LOOPS ###

# Given that you have list:
# # fruits = ['🍎', '🍐', '🍊', '🍌', '🍪']
#
# Suppose you want to print out each item in the list manually:
# # print(fruits[0])
# # print(fruits[1])
# # print(fruits[2])
# # print(fruits[3])
# # print(fruits[4])

# # # Write 'fruit' in each iteration manually
# #
# # print('fruit:', fruits[0])
# # print('fruit:', fruits[1])
# # print('fruit:', fruits[2])
# # print('fruit:', fruits[3])
# # print('fruit:', fruits[4])


# print the 'index' of each fruit manually also:

# # # print('fruit:', fruits[0], 0)
# # # print('fruit:', fruits[1], 1)
# # # print('fruit:', fruits[2], 2)
# # # print('fruit:', fruits[3], 3)
# # # print('fruit:', fruits[4], 4)
# #
# These processes above are quite tedious and will be too tedious as the list gets bigger, we can use loops to achieve all these process in few steps:


### FOR LOOPS ###


# Suppose we want to get/access each item in a list individually and print it out one by one
# We can do this using a for loop

# Example 1:

fruits = ['🍎', '🍐', '🍊', '🍌', '🍪']

for fruit in fruits:
     print(fruit)


# print out the word 'fruit' for each iteration:

for fruit in fruits:
     print('fruit:', fruit)
     print(fruit + "pie")
     print(fruits)
# Example 2:

numbers = [1, 2, 3, 4]
for number in numbers:
     print(numbers)


### enumerate() function ###
# # Used to get the index of each item in a list

# Example 1
# fruits = ['🍎', '🍐', '🍊', '🍌', '🍪']

print(list(enumerate(fruits)))

for index, fruit in enumerate(fruits):
     print(index, fruit)

# Example 2:
characters = ["Krillin", "Goku", "Vegeta", "Gohan", "Picelo"]
list(enumerate(characters))
print(list(enumerate(characters)))

### Python range() function   ###

# using range() in a list:
# # Example: Create a list of numbers from 0 to 9

# print(list(range(10)))

# # using range() in a for loop:
#
# # Example1: Create a sequence of numbers from 3 to 15, and print each item in the sequence:
# for number in range(3, 15):
#     print(number)
#
# # Example2: print the string 'haha' five times using a for loop
#
# for _ in range(5):
#     print('haha')
#
# ## How to populate a list using .append() in a for loop ##
#
# fruits = ['🍎', '🍐', '🍊', '🍌', '🍪']
# # Add 10 🍎's to the Fruit
#
# for _ in range(10):
#     fruits.append('🍎')
#   #  print(fruits)  # this is still within the loop
# print(fruits)  # this is outside the loop
