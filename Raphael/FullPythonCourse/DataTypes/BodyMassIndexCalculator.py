# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height. The BMI is a measure of someone's weight taking into account their height. e.g. if a tal person and a short person both weigh the same amount, the short person is usually more overweight. The BMI is calculated by dividing a person's weight (in kg) by the square of their height(in m). Convert the result to a whole number.

if __name__ == '__main__':
    weight = int(input("enter your weight in kg:\n "))
    height = int(input("enter your height in m:\n ")) ** 2
    BodyMassIndex = weight // height
    print(BodyMassIndex)





