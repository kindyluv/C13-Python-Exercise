import random
import secrets

"""
    The PyPassword Generator is a random password generator.
    
        Structure Of the PyPassword Generator
    The final output should look like this:

    Welcome to the PyPaasword Generator!
    How many letters would you like in your password!?
    How many symbols would you like?
    How many numbers would you like?
    Here is your password:

    Algorithm:
            

"""

if __name__ == '__main__':
    print("Hi " + input("what is your name?\n") + ", Welcome to the PyPassword Generator!\n")
    number_of_letters = int(input("How many letters would you like in your password?\n"))
    number_of_symbols = int(input("How many symbols would you like?\n"))
    number_of_numbers = int(input("How many numbers would you like?\n"))

    password_length = number_of_letters + number_of_symbols + number_of_numbers

    print(password_length)
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    combined_string = letters + digits + symbols
















