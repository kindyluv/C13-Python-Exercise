import random
import string

if __name__ == '__main__':


    print("Hi " + input("what is your name?\n") + ", Welcome to the PyPassword Generator!\n")
    number_of_letters = int(input("How many letters would you like in your password?\n"))
    number_of_symbols = int(input("How many symbols would you like?\n"))
    number_of_numbers = int(input("How many numbers would you like?\n"))


    print(f"Your new password is: {password}")

    for letter in range(1, number_of_letters + 1):
        password = password + randomLetters

    for symbol in range(1, number_of_symbols + 1):
        password = password + random_symbols

    for number in range(1, number_of_numbers + 1):
        password = password + randomNumbers

