if __name__=='__main__':
    weight = input("enter your weight:")
    selection = input("choose either 'pound' or 'kilogram'")

    if selection == str("pound"):
        pound = int(weight) * 2.2046
        print(pound)
    elif selection == str("kilogram"):
        kilogram = int(weight) / 1000
        print(kilogram)

