if __name__ == '__main__':
    number = input("ENTER A NUMBER::")
    index = 0
    counter = 0
    while index < len(number) // 2:
        if number[index] == number[len(number) - index - 1]:
            counter += 1
            index += 1

    if counter == len(number) // 2:
        print("its a palindrome number")
    else:
        print("its not a palindrome number")



