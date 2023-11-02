# 8. Change for a Dollar Game 
# Design a change-counting game that gets the user to enter
# the number of coins required to make exactly one dollar.
# The program should ask the user to enter the number of pennies, nickels, dimes, and quarters.
# If the total value of the coins entered is equal to one dollar, the program should congratulate 
#the user for winning the game. 
#Otherwise, the program should display a message indicating whether the amount entered was more than or less than one dollar. 
print("Enter the number of pennies, nickels, dimes and quarters that will equal to one dollar!")
pennies = 0.01
nickels = 0.05
dimes = 0.10
quarter = 0.25
num_pennies = int(input("Enter the number of pennies: "))
num_nickels = int(input("Enter the number of nickels: "))
num_dimes = int(input("Enter the number of dimes: "))
num_quarters = int(input("Enter the number of quarters: "))
total = (num_pennies * pennies) + (num_nickels * nickels) + (num_dimes * dimes) + (num_quarters * quarter)
if total == 1:
    print("Yay! You win!")
elif total < 1:
    print("Amount entered is less than 1 dollar.")
elif total > 1:
    print("Amount entered is more than one dollar.")