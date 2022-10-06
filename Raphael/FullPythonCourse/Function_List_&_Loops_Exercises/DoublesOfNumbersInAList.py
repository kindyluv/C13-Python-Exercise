# Create a function that doubles all the numbers in a list.
if __name__ == '__main__':

# Algorithm #
# 1. create empty list
# 2. loop through & append to that list
# 3. return that list

    def double(numbers: list) -> list:
        result = []
        for number in numbers:
            result.append(number * 2)

        return result

    print(double([1, 2, 3]))

