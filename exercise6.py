# 6. Book Club Points 
# Serendipity Booksellers has a book club that awards points to its customers 
#based on the number of books purchased each month. The points are awarded as follows:
#• If a customer purchases 0 books, 0 points are awarded.
#• If a customer purchases 1 book, 5 points are awarded.
#• If a customer purchases 2 books, 15 points are awarded.
#• If a customer purchases 3 books, 30 points are awarded.
#• If a customer purchases 4 or more books, 60 points are awarded.  
#Design a program that asks the user to enter the number of books they have purchased this month and displays the number of points awarded.
userinput = int(input("Enter the number of books you have purchased this month: "))
if userinput == 0:
    print("You have 0 points!")
elif userinput == 1:
    print("You have 5 points!")
elif userinput == 2:
    print("You have 15 points!")
elif userinput == 3:
    print("You have 30 points!")
elif userinput == 4 or userinput > 4:
    print("You have 60 points!")
