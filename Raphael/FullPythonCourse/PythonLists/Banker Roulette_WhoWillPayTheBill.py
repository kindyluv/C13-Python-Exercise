
import random
if __name__ == '__main__':

    all_names = input("Enter everybody's names:\n")
    separated_names = all_names.split(",")

    person_who_will_pay = random.choice(separated_names)
    print(person_who_will_pay + "is going to buy the meal today!")







