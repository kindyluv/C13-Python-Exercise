if __name__ == '__main__':
    def Fibonacci(number):
        if number < 0:
            print("invalid number")

        if number == 0:
            return 0
        elif number == 1 or number == 2:
            return 1
        else:
            return Fibonacci(number - 1) + Fibonacci(number - 2)

    print(Fibonacci(6))