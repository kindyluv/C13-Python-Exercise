"""
(Fill in the missing code) Replace *** in the following code with a statement that
will print a message like 'Congratulations! Your grade of 91 earns you an A in this
course'. Your statement should print the value stored in the variable grade:
if grade >= 90:
 ***

"""

if __name__ == '__main__':
    grade = int(input("Enter a grade: "))
    if grade >= 90:
        print(f"congratulations your grade {grade} earns you an A in this course")
    else:
        print("failed!")

