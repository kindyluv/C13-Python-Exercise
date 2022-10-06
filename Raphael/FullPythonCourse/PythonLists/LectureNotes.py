
###     PYTHON LISTS    ###


fruits = ['🍏', '🥭', '🍊','🍌', '🍪']
print(fruits)

states_of_Nigeria = ["Lagos", "Delta", "Imo", "Ibadan"]
print(states_of_Nigeria)

things = [1, 2, 3, "Hello", "Delta", "Orange"]


#  ACCESSING LIST ITEMS
# We use the item imdex to get an item from a list. e.g.
# You can save the item in a variable or print it out.

# POSITIVE INDEX

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])


state = states_of_Nigeria[0]
print(states_of_Nigeria[1])

# NEGATIVE INDEX
# Use a negative index to start counting from the end of the list.
# Use -1 to get the last item in a list

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])

print(states_of_Nigeria[-1])
print(states_of_Nigeria[-2])


# SLICING

# print(fruits[0:2]) # first inclusive. 2nd exclusive
# print(fruits[0:3])
# print(fruits[0:4])

# CHANGING LIST ITEMS

states_of_Nigeria[0] = "Abuja"
print(states_of_Nigeria[0])



## LIST METHODS ##
# 1. .append()
# Use listName.append() to add an item to the end of the list.

fruits.append('🍊')
print(fruits)
fruits.append('🍓')
print(fruits)

states_of_Nigeria.append("Kano")

# 2. .extend()
# Use listName.extend() to add a bunch of items to the end of the list

fruits.extend(['🥭', '🥭', '🍊'])

states_of_Nigeria.extend(["Ekiti", "Jos", "Jigawa"])



## LENGTH OF LIST ##
# 👉 is the number of items in a list.

## LEN() FUNCTION ##
# 👉 use the len() function to get the length of a list


### print(len(fruits))

# # # # # print(fruits[0:len(fruits) - 1])
# # # # #
# # # # # # you can also slice strings as well
# # # # #
# # # # # print('Hi my name is Raphael'[0:22])
# # # # #
# # # # # print('Hi my name is Raphael'[-1]) # gets the last character
# # # # #
# # # # # # step forward
# # # # # print(fruits[0:5:1])
# # # # # print(fruits[0:5:2])
# # # # # print(fruits[0:5:3])
# # #
# # #
# # # # # # Step Backwards
# # # # # print(fruits[::-1]) # reverse the list
# # # # # print(fruits[::-2])
# # #
#  lists can hold different data types inside of them e.g.
#  fruits = ['🍏', '🥭', '🍊','🍌', '🍪', 2, 5, 'hi', 8.5, []]
#  print(fruits)

## lIST CONCATENATION ##

programming_language1 = ['ruby', 'python', 'javascript']
programming_language2 = ['ruby', 'SQL','JAVA', 'javascript']

programming_languages = programming_language1 + programming_language2
print(programming_languages)
