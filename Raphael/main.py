
### OPERATOR ###

# num1 = input('enter a number: ')
# num2 = input('enter a number: ')
# print(num1, num2)
# print(num1 + num2)




# LAMBDA/ANONYMOUS FUNCTIONS

# def sum(a, b):
#     return a + b
# A nice way of writing this same code in one line is:

# implicit return
# sum2 = lambda a, b: a + b
# print(sum2(1, 2))

# greeting = lambda greet, name: f"{greet} {name}"
# print(greeting('aloha', 'martha'))


### TYPE HINTING ###
# 👉Type Hinting is a way to indicate the data type of a value within your Python code.
# 👉It is useful for documentation of your code.
# An example of adding type hinting to a function:


# def greet(name: str) -> str:
#    return "Hello," + name


# greet('name')

# The name: str syntax indicates the name argument should be of type str.
# The -> syntax indicates the greet() function will return a string.


### DICTIONARY ###
#  Key: Value


# person = {
#     'name': 'Raphael',
#     'shirt': 'Black',
#     'laptop': 'Apple'
# }
# print(person)
# print(person['name'])
# print(person['shirt'])
# print(person['laptop'])

#  We can create a function that introduces this person:

# # # def netWorth():
# # #     return person['assets'] - person['debt']
# # #
# # #
# # # def introducer():
# # #     person = {
# # #         'name': 'Raphael',
# # #         'shirt': 'Black',
# # #         'laptop': 'Apple',
# # #         'phone_number': '224-123-3456',
# # #         'assets': 100,
# # #         'debts': 50,
# # #         'favourite-fruits': ['🥭', '🍌', '🍊', '🍓'],
# # #         'netWorth': lambda: person['assets'] - person['debts']
# # #     }
# # #
# # #     person['shirt'] = 'Orange'
# # #     person['assets'] = 1000
# # #
# # #     print(f"👋 Hi my name is {person['name']}, \n👕 I am wearing a {person['shirt']} shirt, \n👨‍💻 and the laptop I use to code is an {person['laptop']}, \n💰and my net worth is ${person['netWorth']()} USD, \n🥝My favorite fruits are {person['favourite-fruits']}")
# # #     # inject the persons data into the f-string
# # #     print(person.keys())
# # #     print(person.values())
# # #     print(list(person.values()))
# # #
# # # introducer()
# # #
# # # # Dictionaries are ordered e.g.
# # # # things = {
# # # #    'health': 100,
# # # #    'name': 'Raphael'
# # # # }
# # # # print(list(reversed(things)))
# # # # this is important in scenarios where you have to sort data.
# #
# # # TUPLES
# #
# # # numbers = (1, 2)
# # # print(numbers)
# # # print(type(numbers))
# #
# # # print(numbers[0])
# #
# # # tuples are immutable
# # # numbers[0] = 10 # this is invalid
# #

### PYTHON SETS ###

# Given two list
programming_language1 = ['ruby', 'python', 'javascript']
programming_language2 = ['ruby', 'SQL','JAVA', 'javascript']

programming_languages = programming_language1 + programming_language2 # concatenation
print(programming_languages)

# how do remove duplicate languages from the list, to get  only unique languages?

# given a tuple
things = (1, 2,2, 4, 7, 8, 8, 9, 8)

# how do you remove the duplicate numbers from the list, to get only unique numbers?

# set are made for this.

## CREATING A SET ##

#  1. using {}
# Example 1:
# # numbers = {1, 2, 2}
# # print(numbers)

# 2. using set()

# Example 1:
# # set([1, 2, 3])
# # print(set([1, 2, 3]))

# Example 2:
# # numbers = set([1, 2, 2, 2])
# # print(numbers)

# Example 3:
set(programming_languages)
print(set(programming_languages))

# Example 4:
set(things)
print(set(things))



# # ## In Operator: is used check whether an element exist in a set e.g.
# # # syntax: element in setName
# #
# # print(2 in numbers)
# # print(1 in numbers)
# # print(4 in numbers)
# #
# # print('SQL' in programming_languages)
# # print('GO' in programming_languages)
# #
# # print(1 in things)
# #
# # # unique() function
# #
# # '''
# #  Create a function unique, that
# #  takes in a list and returns only unique items
# #  >>> unique(['ruby', 'ruby', 'python'])
# #     ['ruby', 'python']
# #  '''
# # # def unique(languages):
# # #    return list(set(languages))
# #
# #
# # # print(unique(['ruby', 'ruby', 'python']))
# #
# #
# # # Converting Unique () function into Lambda functions:
# #
# # # unique = lambda languages: list(set(languages))
# #
# # # print(unique(['ruby', 'ruby', 'python']))
# #
#

# PRACTICE LISTS AND LOOPS