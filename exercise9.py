# 9. Shipping Charges 
#The Fast Freight Shipping Company charges the following rates:
# 2 pounds or less = $1.10
# Over 2 pounds but not more than 6 pounds = $2.20
#Over 6 pounds but nor more than 10 pounds = $3.70
#Over 10 pounds = $3.80
#Design a program that asks the user to enter the weight of 
#a package and then displays the shipping charges
weight = int(input("Calculate the shipping charges!\nEnter the weight of the package in pounds: "))
if weight <= 2:
    print("Shipping charges: $1.10")
elif weight >2 and weight <=6:
    print("Shipping charges: $2.20")
elif weight > 6 and weight <=10:
    print("Shipping charges: $3.70")
elif weight > 10:
    print("Shipping charges: $3.80")