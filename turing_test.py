if __name__ == '__main__':
    name = input("Enter your name: ")
    first_question = input("What is your problem, %s?: " % name)
    second_question = input("%s have you had this problem before (yes or no)?: " % name)

    if second_question == "yes":
        print("well %s, you have it again." % name)
    else:
        print("well %s,you have it now." % name)