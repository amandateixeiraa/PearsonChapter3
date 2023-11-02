# 7.Software Sales 
# A software company sells a package that retails for $99. 
#Quantity discounts are given according to the following table:
# Quantity Discount10–19 20% 20–49 30% 50–99 40% 100 or more 50% 
# Design a program that asks the user to enter the number of packages purchased. 
#The program should then display the amount of the discount (if any) and the total amount of the purchase after the discount.
pack = 99
userinput = int(input("How many packages have you purchased? "))
subtotal = pack * userinput
if userinput < 10: 
    print("No discount available!")
elif userinput >= 10 and userinput <= 19:
    print("You will have 20% off!")
    discount = subtotal * 0.2
    total = subtotal - discount
    print("You'll have a discount of",round(discount,2),"dollars. Your total is:",round(total,2),"dollars." )
elif userinput >= 20 and userinput <=49:
    print("You will have 30% off!")
    discount = subtotal * 0.3
    total = subtotal - discount
    print("You'll have a discount of",round(discount,2),"dollars. Your total is:",round(total,2),"dollars." )
elif userinput >= 50 and userinput <=99:
    print("You will have 40% off!")
    discount = subtotal * 0.4
    total = subtotal - discount
    print("You'll have a discount of",round(discount,2),"dollars. Your total is:",round(total,2),"dollars." )
elif userinput >= 100:
    print("You will have 50% off!")
    discount = subtotal * 0.5
    total = subtotal - discount
    print("You'll have a discount of",round(discount,2),"dollars. Your total is:",round(total,2),"dollars." )




