# WAP that calculates the average student height from a list of heights using for loop. The average height can be calculated by adding all the heights together and dividing by the total number of heights. Average height should be rounded to the nearest whole number
if __name__ == '__main__':
    student_heights = list(range(100, 170, 5))
    total_height = 0
    number_of_student = 0
    for height in student_heights:
        total_height += height
        number_of_student += 1

    average_height = round(total_height / number_of_student)
    print(average_height)



