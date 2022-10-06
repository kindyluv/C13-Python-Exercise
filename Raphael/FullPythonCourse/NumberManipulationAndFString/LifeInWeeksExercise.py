

if __name__ == '__main__':
    current_age = int(input("enter your current age:\n"))
    expectedYearsToLive = 90 - current_age
    NumberOfDays = expectedYearsToLive * 365
    NumberOfWeeks = expectedYearsToLive * 52
    NumberOfMonths = expectedYearsToLive * 12
    print(f"You have {NumberOfDays} days, {NumberOfWeeks} weeks and {NumberOfMonths} months left")
