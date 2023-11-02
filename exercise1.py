# 1. Roman Numerals
# Design a program that prompts the user to enter a number within the range of 1 through 10.
#The program should display the Roman numeral version of that number. If the number is outside 
#the range of 1 through 10, the program should display an error message.


user_input = int(input("Enter a number within the range of 1 through 10: "))
if user_input == 1:
    print("I")
elif user_input == 2:
    print("II")
elif user_input == 3:
    print("III")
elif user_input == 4:
    print("IV")
elif user_input == 5:
    print("V")
elif user_input == 6:
    print("VI")
elif user_input == 7:
    print("VII")
elif user_input == 8:
    print("VIII")
elif user_input == 9:
    print("IX")
elif user_input == 10:
    print("X")
elif user_input < 1 or user_input > 10:
    print("This number is invalid!")
    
    