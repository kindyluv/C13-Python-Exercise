if __name__ == '__main__':
    data = []
    day = 1
    while day <= 7:
        user_input = int(input(f"ENTER THE NUMBER OF INFECTED PERSONS FOR DAY {day}: "))
        data.append(user_input)
        day += 1

    print(f'the total number of infected persons are --> {sum(data)}')
    print(f'the average number of infections are -->  {sum(data) / len(data)}')
    print(f'the largest number is --> {max(data)}')
    print(f' the smallest number is --> {min(data)}')
