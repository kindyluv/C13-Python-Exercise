if __name__ == '__main__':
    number = int(input("Enter integer: "))

    digits1 = number % 10

    digits2 = number % 100 // 10

    digits3 = number % 1000 // 100

    digits4 = number % 10000 // 1000

    print(digits1, digits2, digits3, digits4)

