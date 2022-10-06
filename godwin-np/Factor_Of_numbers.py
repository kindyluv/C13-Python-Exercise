if __name__ == '__main__':
    num = int(input("enter a  number::"))
    for x in range(1, num +1):
        if num % x == 0:
            total = 0
            total += x
            print(total)



