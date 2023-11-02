#Magic Dates
#The date June 10, 1960, is special because when it is written in the following format,
#the month times the day equals the year: 
#6/10/60
# Design a program that asks the user to enter 
#a month (in numeric form), a day, and a two-digit year. The program should then determine
# whether the month times the day equals the year. If so, it should display a message saying
#the date is magic. Otherwise, it should display a message saying the date is not magic.

month = int(input("Enter the month in numeric form:"))
day = int(input("Enter the day: "))
year = int(input("Enter two-digit year: "))
equals = month * day
if len(str(year))!= 2:
    print("Error! Only two digits allowed.")
elif year == equals:
    print("This date is magic!")
elif year != equals:
    print("This date is not magic!")