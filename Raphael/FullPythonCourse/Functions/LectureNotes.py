if __name__ == '__main__':

### PYTHON FUNCTIONS ###

#   Function Creation and Invocation #

#   Example 1
    def say_my_name():
        print('Martha')

    say_my_name()

# Example 2
    def subtractNum():
        print(34 - 4)

    subtractNum()

# Example 3
    def greeting():
        print("Hello Ashley Immanuel")

    greeting()

# ARGUMENTS IN PYTHON FUNCTIONS #

# SINGLE ARGUMENT #

# Example 1:

    def my_name(name):
        print(name)

    my_name('raphael ekpei')

# Example 2:

    def say_my_name(name):
        print('Hi ' + name)
        print(' Welcome to Semicolon')

    say_my_name("Raphael")
    say_my_name("Funmi")
    say_my_name("Jude")
    say_my_name("Nenman")
    say_my_name("Martha")
    say_my_name("Martins")
    say_my_name("Kelvin")


# Example 3:
    def greetingNatives(name):
        print('Good Afternoon ' + name)

    greetingNatives('Amira')
    greetingNatives('Jude')
    greetingNatives('Ernest')

# Example 4:
    def my_Family_Name(firstname):
        print(f'{firstname}' + 'Ekpei')

    my_Family_Name('Kingsley')
    my_Family_Name('Grace')
    my_Family_Name('Evelyn')
    my_Family_Name('Raphael')


# MULTIPLE ARGUMENTS

# Example 1:

    def addNum(num1, num2):
        print(num1 + num2)

    addNum(2, 4)

# Example 2:

    def greeting(greet, name):
        print(f'👋{greet} {name}')


    greeting('aloha', 'Martha')

#  TYPES OF ARGUMENTS IN PYTHON FUNCTIONS #

# 1. VARIABLE LENGTH ARGUMENTS(*args) #

# Example 1:
    def variableArgs(*a):
            print(a)
            return

    variableArgs(10, 34.56, 'python')
# Example 2

    def my_function(*kids):
        print('the youngest child is' + kids[2])


    my_function('Kingsley', 'Raphael', 'Grace', 'Linus')



# 2. DEFAULT ARGUMENTS #

# Example 1:
    def greeting(name, greet='aloha'):
        print(f'{greet} {name}!')


    greeting('Raphael')
#   greeting('Raphael', "Hello') # this will ignore the default argument

# Example 2:

    def defaultArgs(num1, num2, num3=30):
        print(num1, num2, num3)
        return

    defaultArgs(10, 20,)
#   defaultArgs(10, 20, 40) # the default argument will be ignored and the specified argument will be pushed


# 3. POSITIONAL ARGUMENTS #

# Example 1:
    def power(num1, num2):
        print(num1 ** num2)
        return

    power(2, 3) # 8
    power(3, 2) # 9



# 4. NAMED/KEYWORD ARGUMENTS #

# Example 1:

    def namedArgs(name, age, dept=10):
        print("Name: ", name)
        print("Age: ", age)
        print("Department: ", dept)
        return

    namedArgs(age=25, name="Jude")



# greeting(name='Martha', greet='👋 Hi')

# THE RETURN STATEMENT IN PYTHON FUNCTIONS #

# Example 1:
    def cube(num):
        return num * num * num
        print('code') # this won't ne executed

    print(cube(3))

# Example 2:

    def square(num):
        return num * num

    result = square(4)
    print(result)

# Example 3:

    def multiply(number1, number2):
        return number1 * number2

    print(multiply(2, 5))

# Example 4:
    def multiply(num1):
        return num1 * 5


    total = multiply(5)
    print(total)

# Example 5:
    def addNum():
        return 3 + 3
        print('Hello World')


    print(addNum())



# EXERCISE 1:      create a function called sum which takes in two integers and returns their sum
# def sum(num1 : int , num2 : int) ->int:
#    return num1 + num2

# result = sum(1, 2)
# print(result)



# EXERCISE 2: Write a function bigger_guy that takes in two numbers and returns the bigger one.
# MAKE SURE to use RETURN and not PRINT in your function.

def bigger_guy(number1, number2):
     if number1 > number2:
         return number1
     else:
         return number2
 print(bigger_guy(16, 8))
