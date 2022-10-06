
"""
11. Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.


"""

if __name__ == '__main__':
    first_number = int(input("Enter first number:"))
    second_number = int(input("Enter second number"))
    third_number = int(input("Enter third number"))
    fourth_number = int(input("Enter fourth number"))

    first_number = first_number - 1
    second_number = second_number - 2
    third_number = third_number + 2
    fourth_number = fourth_number + 1
    print(first_number,second_number,third_number,fourth_number)



