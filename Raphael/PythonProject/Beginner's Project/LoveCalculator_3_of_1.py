if __name__ == '__main__':
    """
    Requirements:
    1. Display a welcome message
    2. Ask users for their name, and then their crush's name.
    3. The first step is to calculate the first thing we need to do is to combine the names/strings.
    4. Then count the number of times each of the letters T R U E  and L O V E occurs in these names(Hint: Use the lower function and the count function.)
    5. Then combine both digits together to get the love score.
    6. Interpret the love score based on the condition specified.
    
    HINT:
    
    e.g. When you hit run, this is what should happen:
    
    """

    print("Hi!, Welcome to the Love Calculator!")
    your_name = input('What is your name?\n')
    crush_name = input("What is your crush name?\n")
    combined_names = your_name + crush_name

    lower_names = combined_names.lower()
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.lower().count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digits = l + o + v + e

# you convert the first_digit and second digit to str, so they can concatenate and to prevent normal addition. You then convert the string to integer.7
    love_score = int(str(first_digit) + str(second_digits))

    if love_score < 10 or love_score > 90:
        print(f"your score is {love_score}, you go like coke and mentos.")

    elif (love_score >= 40) and (love_score > 50):
        print(f"your score is {love_score}, you are alright together")
    else:
        print(f"your score is{love_score}")














