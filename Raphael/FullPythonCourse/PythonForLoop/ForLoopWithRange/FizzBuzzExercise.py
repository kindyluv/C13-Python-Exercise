"""
WAP that automatically prints the solution to the FizzBuzz game.

    Your program should print each number from 1 to 100 in turn

    When the number is divisible by 3, then instead of printing the number it should print "fizz"

        When the number is divisible by 5, then instead of printing the number it should print "Buzz"

    And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"


"""

if __name__ == '__main__':

    for number in range(1, 101):
        if (number % 3 == 0) and (number % 5 == 0):
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

# Note that the if/elif/else statement will stop once it has found one statement that is true.
# So the logic is very important here.


