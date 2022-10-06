if __name__ == '__main__':
    number = int(input("Enter a number: "))
    temp = number
    summation = 0

    while number != 0:
        rem = number % 10
        summation = (summation * 10) + rem
        number //= 10

    if summation == temp:
        print("it is a palindrome number")
    else:
        print("it is not a palindrome number")
