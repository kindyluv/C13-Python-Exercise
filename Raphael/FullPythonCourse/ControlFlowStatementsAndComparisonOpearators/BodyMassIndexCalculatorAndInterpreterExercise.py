# WAP that interprets the body Mass Index (BMI) based on a user's weight and height.

if __name__ == '__main__':
    print("Hi" + input("what is your name?") + "Welcome to the Body Mass Interpreter")
    height = float(input("What is your height?\n"))
    weight = float(input("what is your weight?\n"))
    bodyMassIndex = round(weight / (height ** 2))
    if bodyMassIndex < 18.5:
        print(f"Your BMI is {bodyMassIndex}, you are underweight")
    elif bodyMassIndex < 25:
        print(f"Your BMI is {bodyMassIndex}, you have a normal weight")
    elif bodyMassIndex < 30:
        print(f"Your BMI is {bodyMassIndex}, you are overweight")
    elif bodyMassIndex < 35:
        print(f"your BMI is {bodyMassIndex}, you are obese")
    else:
        print(f"your BMI is {bodyMassIndex}, you are clinically obese")





