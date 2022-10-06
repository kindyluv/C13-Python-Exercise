if __name__ == '__main__':

    """
    Building a Tip Calculator
    The Tip Calculator calculates tip amount for various percentages of the cost of the service, and also provides a total amount that includes the tip.
    The tip calculator is a useful tool for everyone who goes out to a restaurant, bar, or anywhere else you are supposed to tip. 
    
    Structure Of the Tip Calculator
    The final output should look like this:
    
    Welcome to the tip calculator!
    What is your service/product amount? For this app, the product is food
    What percentage tip would you like to give? 10, 12, or 15?
    How many people to split the bill?
    Each person should pay:

    Algorithm:
    Display a message to welcome the user to the tip calculator
    Ask the user to enter food amount
    Ask the user to enter tip_percentage(divide the percentage by 100)
    calculate tip_amount(tip_amount = food_amount * tip_percentage)
    calculate total bill( total_bill = food_amount - tip_amount) / numberOfPersonToSplitTheBill
    Display food amount, tip amount and total bill
        
    Note: The total bill should be rounded to two decimal places of accuracy    
    
    """

    print("Hi!😍😍" + input("enter your name:\n") + " Welcome to the tip Calculator")
    food_amount = float(input("What is your food amount?\n "))
    tip_percentage = float(input("What percentage tip would you like to give? 10%, 12%, or 15%\n")) / 100
    tip_amount = food_amount * tip_percentage
    numberOfPersonToSplitTheBill = int(input("How many people to split the bill?\n"))
    total_bill = (food_amount - tip_amount) / numberOfPersonToSplitTheBill
    round(total_bill, 2)
    print("\n\n\n")
    print("---------------------------------------------------------")
    print(f"🍩🍩 Food Amount: N{food_amount}")
    print(f"⚖⚖ Tip Amount : N{tip_amount}")

    print("\n")
    print(f"💰💰 Each Person Should Pay: N{total_bill}")
    print("---------------------------------------------------------")
