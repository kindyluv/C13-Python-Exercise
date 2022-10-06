if __name__ == '__main__':
    count = 0
    while count <= 5:
        grade = int(input("enter a grade::"))
        if grade <= 0:
            print("invalid digit")

        if 90 <= grade <= 100:
            print("A")
        elif 70 <= grade <= 89:
            print("B")
        elif 50 <= grade <= 69:
            print("c")
        elif 30 <= grade <= 49:
            print("d")
        elif 10 <= grade <= 39:
            print("you are a failure u can never make it")
        count += 1
        if count == 3:
            break


