
if __name__ == '__main__':

    ## STRING MANIPULATION  ##

# 1. NEWLINE \n #
# Example:
print("Hello World")
print("Hello World")
print("Hello World")
# The 3 statements can be done in a single statement using \n
print("Hello world\nHello World\nHello World")

# 2. STRING CONCATENATION #

# means adding strings together.
# it is done by using the plus sign (+)

# Adding a String and a String #

# Example 1:

print("Hello " + "Angela")
print("Hello" + " Angela")
print("Hello" + " " + "Angela")

# Example 3:
print('String concatenation is done with the "+" sign')
print("String concatenation is done with the "+" sign") # this will lead to mismatched text because python sees the + sign as the concatenation operator rather than a text to be printed out. To solve this, you must replace one with a single quotes.

# Example 2:
your_name = 'Martha'
print('hi' + your_name)

# Example 4:
print("123" + "345")

# Adding a String and an Integer
# 👉To add a string and an integer together, we must first convert the integer to a string.

# ways to convert integer to string in Python #
# 1. str()
# 2. Using double quote “
# 3. repr()

# using double quote "

# Example 1:
character_name = "John"
character_age = "35"  # we add a double quote to 35 because we are concatenating it with strings
print("There once was a man named" + character_name + ",")
print("he was" + character_age + "years old.")
print("He really liked the name" + character_name + ",")
print("but didn't like being" + character_age + ".")

# Using str() function
# Example1:

the_str = "My daughter's age is: "
age = 3
print(the_str + str(age))

# Example 3:
amount = 25
# print('$' + amount) # this gives an error because amount is an integer.
print('$' + str(amount))


# SUBSCRIPTING STRINGS #
# Subscripting is the method of pulling out a particular element/character from a string

print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])

# programmers always start counting from 0 to 1, 2, etc.
# To get the character of a string,
