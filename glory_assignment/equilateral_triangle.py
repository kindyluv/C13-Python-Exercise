"""
8. (Triangles) In an equilateral triangle, the lengths of all three sides are equal. Consequently,
it is also equiangular with all three internal angles congruent to each other and
measuring 60°. Write a script where a user can input the length of the three sides of a triangle.
The script should determine if it is an equilateral triangle or not.

"""

if __name__ == '__main__':
    angle1 = int(input("Enter a number as an angle: "))
    angle2 = int(input("Enter a number as an angle: "))
    angle3 = int(input("Enter a number as an angle: "))

    if angle1 == angle2 and angle2 == angle3:
        print("It is an equilateral triangle")
    else:
        print("It is not an equilateral triangle")
