"""
7. (Flu Patients Data Processing) During the flu season, it is important to keep track
of the number of infected patients. Write a script in which the user can input the number
of reported infections per day over one week. Calculate the total, average, smallest, and
largest of these values. Write your script using a loop structure.

"""

if __name__ == '__main__':
    age = int(input("Please enter your age in years: "))
    max_heart_rate = 220 - age

    print("Your target heart rate is: ")
    target_heart_rate1 = max_heart_rate * (50 / 100)
    target_heart_rate2 = max_heart_rate * (85 / 100)

    print(f"{target_heart_rate1} - {target_heart_rate2}")
