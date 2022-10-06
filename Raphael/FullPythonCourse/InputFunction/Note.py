### INPUT() FUNCTION ###

# 👉 The input() function is used to collect user input.
# 👉 By default, it returns the user input as a string.
# Syntax: print(prompt)
# in most case, you might have to store the input in a variable.
# variableName = print(prompt)

# Example 1:
input("what is your name?")

# We can have an input() nested inside a print()
# input() will get user input in console
# Then print() will print the world "Hello" and the user input
# Example 1:
print("Hello " + input("What is your name?") + "!")
