### DATA TYPES IN PYTHON ###

# STRING
# 👉 anything within double quotes or single quotes
# e.g.  "Hello", "Raphael is in love", "123"


# INTEGERS(INT)
# 👉 whole numbers e.g. 2, -2
# Use underscore with large numbers to make it more readable.g. 123_456_789

# FLOAT
# 👉 decimal numbers e.g. 50.5, 3.142

# BOOLEAN
# 👉contains True or False values e.g.
# John = "Male"
# is_Male = True

# 5 > 10 -> True
# 5 == 5 -> True

# TYPE CHECKING
#  Use type() function to check the type of data you are working with. #

a = 123
type(123)
print(type("Hello"))

### TYPE CASTING (TYPE CONVERSION) ###

# str() function #
# the str()function converts the specified value into a string

# Example 1:
amount = 25
print('$' + str(amount))

# Example 2:
num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + "characters.")

# Example 3:
print(str(70) + str(100))


# int() function #
# 👉 The int() converts strings to int

# Example 1:
a = 123
type(a)
print(type())

# Example 2:
# num1 = input('enter a number: ')
# num2 = input('enter a number: ')
# print(int(num1), int(num2))


# float() function #
# the float () function converts the specified value into a floating point number.
print()

num = float(123)
print(type(num))

print(70 + float("100.5"))
