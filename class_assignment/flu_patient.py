if __name__ =='__main__':
    total = 0
    smallest = 9999999
    largest = 0
    counter = 0

    while counter != 7:
        number = int(input("Enter the number of cases for the day"))

        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number
        total = number
        counter +=1
    average = total / 7
    print(f'Total cases for the week is %d' % total)
    print(f'Average cases for the week is %d' % average)
    print(f'The smallest is %d' % smallest)
    print(f'The largest is %d' % largest)
