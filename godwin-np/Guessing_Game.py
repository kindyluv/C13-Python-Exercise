import random
if __name__ == '__main__':

    my_Number = random.randint(1, 6)

    count = 0
    while count < 3:
        digit = int(input("enter a number -->"))

        if digit == my_Number:
            print("you are correct")
            break
        elif digit < my_Number:
            print("too low")
        elif digit > my_Number:
            print("too high")

        count += 1
