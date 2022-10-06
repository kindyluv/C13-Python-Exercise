# Write a program that adds the digits in a 2-digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
if __name__ == '__main__':

# Algorithm
# 1. Get the user to input a two-digit number
# Get the first and second digits using subscripting then convert string to int.
# 3. Add  the two digits together
    number = input("enter any two digit number:\n ")
    print(int(number[0]) + int(number[1]))

