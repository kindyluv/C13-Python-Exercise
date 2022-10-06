from class_assignment.heart_rates import HeartRates

if __name__ == '__main__':
    my_heart_rates = HeartRates(29)
    my_heart_rates.set_age(int(input("Enter your age:")))
    print("Patient age is: ", my_heart_rates.get_age())
    print("The maximum heart rate is:", my_heart_rates.get_maximum_heart_rates__())
    print("The Target heart rates is:", my_heart_rates.get_target_heart_rates())
