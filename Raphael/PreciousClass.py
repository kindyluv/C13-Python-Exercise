if __name__ == '__main__':

    number = int(input("enter a number: "))
    counter = 2
    factor = 0
    sum = 0


    while counter < number:
        factor = number / counter
        sum = sum + factor
        counter += 2
        print("factor is: ", int(factor))
        print("sum is:", int(sum))

#     myName = "Raphael"
#     print(myName)
#
# height, weight = 100, 200
# print('height is:',  height)
# print('weight is:', weight)
#
# your_name = 'Martha'
# print('Hi ' + your_name)
#
# number1 = input('enter')


#    num1 = int(input('enter num1:'))
#    num2 = int(input('enter num2:'))
# sum = num1 + num2
# mut = num1 * num2
# rais1 = num1 ** 2
# rais2 = num2 ** 2
# div = num2 / num1
# f_div = num2 // num1
# avg = (num1 + num2) / 2
