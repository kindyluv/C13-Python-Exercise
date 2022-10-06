# WAP that calculates the highest score from a List of student scores. The output should have the world the highest score in the class is : x
if __name__ == '__main__':

    student_scores = list(range(51, 100, 2))
    highest_score = max(student_scores)
    print(f"The highest score in the class is: {highest_score}")

