
if __name__ == '__main__':
    print('''
    
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
    ''')

    print("Hi " + input("what is your name?\n") + " Welcome to Treasure Island. \nYour mission is to find the treasure.")
    choice1 = input("You are at a cross road. Where do you want to go? Type \"left\" or R for \"right\":\n").lower()
    # the user could type the answer as RIGHT, Right or Right. To make sure that when we are doing our check with if statements we ignore the casing , we use the .lower() function to change the input. So no matter how they wrote it, it should change the input all to lower case.
    # You could also say if choice1 == left or choice1 == Left or choice1 == LEFT, but for simplicity and lesser code writing it's better this way
    if choice1 == "left":
        print("you fell into a hole. Game over")
    else:
        choice2 = input('You\'ve come to a lake. There is an Island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across').lower()
        if choice2 == "wait":
            choice3 = input("You arrive at the island unharmed.There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
            if choice3 == "red":
                print("It's a room full of fire. Game over")
            elif choice3 == "yellow":
                print("you found the treasure. you win")
            elif choice3 == "blue":
                print("You enter a room of beasts. Game over.")
            else:
                print("You made an invalid choice. Game over")
        else:
            print("You drowned. Game over")




