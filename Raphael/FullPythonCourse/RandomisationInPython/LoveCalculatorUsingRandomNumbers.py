import random

if __name__ == '__main__':
    """
    Requirements:
    1. Display a welcome message
    2. Ask users for their name, and then their crush's name.
    3. We can use random numbers to get the love_score instead of counting the number of times the letters T R U E  and L O V E occurs in the given names.
    4. Interpret the love score based on the condition specified
    
    """

    print("Hi!, Welcome to the Love Calculator!")
    your_name = input('What is your name?\n')
    crush_name = input("What is your crush name?\n")

    love_score = random.randint(1, 100)

    if love_score < 10 or love_score > 90:
        print(f"your love score is {love_score}, you go like coke and mentos.")

    elif (love_score >= 40) and (love_score > 50):
        print(f"your score is {love_score}, you are alright together")
    else:
        print(f"your score is {love_score}")















