if __name__ == '__main__':
    '''
    Requirements
    1. Create a greeting for your program.
    2. Ask the user for the city that they grew up in.
    3. Ask the user for the name of a pet
    4. Combine the name of their city and pet and show them their brand name.
    5. Make sure the input cursor shows on a new line.
    '''

print('Hi! ' + input('enter your name\n') + "," + ' Welcome to RaphKing Band Name Generator')
city = input('what city did you grew up in?\n')
pet = input('enter the name of your pet or any pet you like\n')
print('Your band name is: ' + city + " " + pet)

