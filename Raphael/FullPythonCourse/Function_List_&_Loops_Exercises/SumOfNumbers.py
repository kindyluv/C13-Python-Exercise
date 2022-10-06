# Create a function that takes in a list of numbers and return their sum.

if __name__ == '__main__':

    def sum_list(numbers: list[int]) -> int:
        count = 0
        for number in numbers:
            count = count + number

        return count


    print(sum_list([1, 2, 3]))
    print(sum_list([1, 2, 3, 4]))
