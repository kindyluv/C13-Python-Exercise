"""
5. (Target Heart-Rate Calculator) While exercising, you can use a heart-rate monitor
to see that your heart rate stays within a safe range suggested by your doctors and trainers.
According to the American Heart Association (AHA) (http://bit.ly/AHATargetHeart Rates), the formula for
calculating your maximum heart rate in beats per minute is 220
minus your age in years. Your target heart rate is 50–85% of your maximum heart rate.
Write a script that prompts for and inputs the user’s age and calculates and displays the
user’s maximum heart rate and the range of the user’s target heart rate. [These formulas
are estimates provided by the AHA; maximum and target heart rates may vary based on
the health, fitness and gender of the individual. Always consult a physician or qualified
healthcare professional before beginning or modifying an exercise program.]


"""

if __name__ == '__main__':
    days = 1
    value = 0
    total = 0
    largest = 0

    while days <= 7:
        value = int(input(f"Enter value for day {days}: "))
        days += 1
        total += value

        if value > largest:
            largest = value

    average = total / days

    print(f"The total of the values is {total},\n"
          f"the average of the values is {average},\n"
          f"the smallest value is {smallest},\n"
          f"the largest value is {largest}.")
