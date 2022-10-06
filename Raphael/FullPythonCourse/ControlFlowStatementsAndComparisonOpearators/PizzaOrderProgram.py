if __name__ == '__main__':

    print("Welcome to Python Pizza Deliveries")
    size = input("What size pizza do you want? S, M or L -->\n")
    add_pepperoni = input("Do you want pepperoni? Y or N -->\n")

    total_bill = 0
    if size == "S":
        total_bill = 15
        print("your total_bill is $15")
    elif size == "M":
        total_bill = 20
        print("your total bill is $20")
    else:
        total_bill = 25
        print("your total_bill is $25")

    if add_pepperoni == "Y":
        if size == "S":
            total_bill = total_bill + 2
        else:
            total_bill = total_bill + 3

    extra_cheese = input("Do you want extra cheese? Y or N")
    if extra_cheese == "Y":
        total_bill += 1
    print(f"your final bill is ${total_bill}")





