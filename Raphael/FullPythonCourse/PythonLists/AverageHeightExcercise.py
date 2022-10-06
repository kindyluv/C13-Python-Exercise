# WAP that calculates the average student height from a list of heights. The average height can be calculated by adding all the heights together and dividing by the total number of heights.Average height should be rounded to the nearest whole number

if __name__ == '__main__':
    student_height = list(range(100, 170, 5))
    total_height = sum(student_height)
    total_students = len(student_height)
    average_height = round(total_height / total_students)
    print(average_height)

