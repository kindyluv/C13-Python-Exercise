

if __name__ == '__main__':
    user_input = int(input("Enter a number -: "))
    total_sum = 0

    for x in range(1, user_input):
        if user_input % x == 0:
            print(x)
            total_sum += x

    print("Total Sum == ",total_sum)
    if total_sum == user_input:
        print("This is a perfect number -:")
    else:
        print("Zero Talent")


