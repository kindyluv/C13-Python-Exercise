import random
if __name__ == '__main__':

    """
    Head Tail Game 
    1. Ask the user to input their choice, either Head or Tail
    2. Then with the help of random function, computer choice and our choice will be compared.    
    3. A print statement will give the result as output.
    
    """
if __name__ == '__main__':
    print("Welcome to the virtual coin toss program")
    seedNumber = int(input("Create a seed number: "))
    random.seed(seedNumber)

    random_side = random.randint(0, 1)

    if random_side == 0:
        print("Tails")
    else:
        print("Heads")