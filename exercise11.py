# 11. Leap Year Detector 
# Design a program that asks the user to enter a year, and then displays a message indicating whether that year is a leap year or not.
# Use the following logic to develop your algorithm:
#• If the year is evenly divisible by 100 and is also evenly divisible by 400, 
#then it is a leap year. For example, 2000 is a leap year but 2010 is not.
#• If the year is not evenly divisible by 100, but it is evenly divisible by 4, it is a leap year.
# For example, 2008 is a leap year but 2009 is not.

year = int(input("Enter year: "))
if year % 100 == 0 and year % 400 == 0:
    print("That's a leap year!")
elif year % 100 != 0 and year % 4 == 0:
    print("That's a leap year!")
else:
    print("That's not a leap year!")