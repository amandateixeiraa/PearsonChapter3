# 2. Areas of Rectangles
#The area of a rectangle is the rectangle’s length times its width.
# Design a program that asks for the length and width of two rectangles.
# The program should tell the user which rectangle has the greater area,
#or whether the areas are the same.

rect1_lenght = int(input("What is the lenght of the first rectangle? "))
rect1_width = int(input("What is the width of the first rectangle? "))
rect2_lenght = int(input("What is the lenght of the second rectangle? "))
rect2_width = int(input("What is the width of the second rectangle? "))
rect1_area = rect1_lenght  * rect1_width
rect2_area = rect2_lenght *  rect2_width

if rect1_area > rect2_area:
    print("The first rectangle has the greater area.")
elif rect2_area > rect1_area:
    print("The second rectangle has the greater area.")
elif rect1_area == rect2_area:
    print("The two rectangles have the same area.")