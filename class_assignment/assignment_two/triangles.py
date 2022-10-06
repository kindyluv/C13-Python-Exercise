def is_valid_triangle(a, b, c):
    if a + b >= c and b + c >= a and c + a >= b:
        return True
    else:
        return False

def triangle_type(a, b, c):
    if a == b and b == c:
        print("The triangle is equilateral")
    else:
        print("The triangle is not equilateral")

if __name__ == '__main__':
    first_slide = int(input("Enter first length: "))
    second_slide = int(input("Enter second length:"))
    third_slide = int(input("Enter first length:"))

    if is_valid_triangle(first_slide, second_slide, third_slide):
        triangle_type(first_slide, second_slide, third_slide)
