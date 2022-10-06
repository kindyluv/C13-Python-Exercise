

if __name__ == '__main__':



###  IF/ELSE STATEMENT ###
# Use if/else statement to select one of 2 choices

# RollerCoaster Ticketing Problem
# program to sale a roller coaster ticket based on the customer's height of the user

    print("Welcome to the roller coaster!")
    height = int(input("What is your height in cm?"))

    if height >= 120:
        print("You can ride the roller coaster")
    else:
        print("Sorry, you have to grow taller before you can ride.")

# NESTED IF/ELSE STATEMENT
# Use nested if/else to check multiple conditions e.g. height and age

    print("Welcome to the roller coaster!")
    height = int(input("What is your height in cm?"))

    if height >= 120:
        print("You can ride the roller coaster")
        age = int(input("what is your age"))
        if age <= 18:
            print("please pay $7.")
        else:
            print("please pay 12.")

    else:
        print("Sorry, you have to grow taller before you can ride.")

###     IF/ELIF/ELSE STATEMENT  ###

# Use if/elif/else to check for multiple conditions.

# Example:
    print("Welcome to the roller coaster!")
    height = int(input("What is your height in cm?"))
    if height >= 120:
        print("You can ride the roller coaster")
        age = int(input("what is your age"))
        if age < 12:
            print("please pay $5.")
        elif age <= 18:
            print("please pay  $7.")
        else:
            print("please pay $12.")

    else:
        print("Sorry, you have to grow taller before you can ride.")


# Multiple if

# Use Multiple if to check for multiple conditions even if the previous one is already true.
# if you are going on a roller coaster ride, you'd probably want to take a picture.
# We want to be able to charge users an extra 3 dollars if they want to purchase a ticket that includes a photo.
# This is completely independent of their age or their height.
# Even if we've already gotten their age and height and determined their ticket price.
# This is an extra question. Do you want a photo or not? if you do, we are going to add 3 dollars to their existing ticket price.
# To do this we would write multiple if statements.

# Example:

    print("Welcome to the roller coaster!")
    height = int(input("What is your height in cm?"))
    if height >= 120:
        print("You can ride the roller coaster")
        age = int(input("what is your age"))
        total_bill = 0
        if age < 12:
            total_bill = 5
            print(total_bill)
        elif age <= 18:
            total_bill = 7
            print(total_bill)
        else:
            total_bill = 12
            print(total_bill)
        wants_photos = input("Do you want a photo taken? Y or N. ")
        if wants_photos == "Y":
            total_bill += 3

        print(f"your total bill is: {total_bill}")

    else:
        print("Sorry, you have to grow taller before you can ride.")


### COMBINING MULTIPLE CONDITIONS IN THE SAME LINE OF CODE  ###

#   Let's say that the roller_coaster company decided that they are going to give a free ticket to people having midlife crisis(typically occurs at 45-55 years old)
#   Let's incorporate this into our code:
#   if they want to have photo they have to pay 3 dollars, but at least their ticket is free.


    print("Welcome to the roller coaster!")
    height = int(input("What is your height in cm?"))
    if height >= 120:
        print("You can ride the roller coaster")
        age = int(input("what is your age"))
        total_bill = 0
        if age < 12:
            total_bill = 5
            print(total_bill)
        elif age <= 18:
            total_bill = 7
            print(total_bill)
        elif age >= 45 and age > 55:
            total_bill = total_bill + 0
            print("Everything is going to be ok. Have a free ride on us!")
    elif age > 18:
        total_bill = 12
        print(total_bill)

    wants_photos = input("Do you want a photo taken? Y or N. ")
    if wants_photos == "Y":
        total_bill += 3

        print(f"your total bill is: {total_bill}")

    else:
        print("Sorry, you have to grow taller before you can ride.")

