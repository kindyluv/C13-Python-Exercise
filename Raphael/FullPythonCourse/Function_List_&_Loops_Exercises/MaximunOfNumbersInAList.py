# Create a function that finds the maximum of numbers in a list.

if __name__ == '__main__':

    def find_max(numbers: list[int]) -> int:
# set the current_max to the first element in the list
        current_max = numbers[0]
        for number in numbers:
            if number > current_max:
                current_max = number

        return current_max


    print(find_max([1, 5, 10, 3]))

# The reason why you should not set current_max to 0 is becuase if the list contains all non-negative numbers, it wil return zero. e.g. [-1, -2, -3, -4, -5, -6]


