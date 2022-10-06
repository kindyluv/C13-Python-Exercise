"""
WAP that calculates the sum of all the even numbers from 1 to 100, including 1 and 100.
Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

"""

if __name__ == '__main__':

    sum = 0
    for number in range(2, 101, 2):
        sum += number

    print(sum)


# Alternative Approach
    total = 0
    for number in range(1, 101):
        if number % 2 == 0:
            total += number

    print(total)

# There could be other ways to solve this problem, but these two are the most popular.



