if __name__ == '__main__':
    side1 = int(input("Enter the 1st sides of the triangle"))
    side2 = int(input("Enter the 2nd side of the triangle"))
    side3 = int(input("enter the 3rd side of the triangle"))
    if side1 == side2 and side2 == side3:
        print("its an equilateral triangle")
    else:
        print("its not an equilateral triangle")