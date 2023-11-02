# 5. Color Mixer
# The colors red, blue, and yellow are known as the primary colors
# because they cannot be made by mixing other colors. When you mix two
#primary colors, you get a secondary color, as shown here:
#• When you mix red and blue, you get purple.
#• When you mix red and yellow, you get orange.
#• When you mix blue and yellow, you get green.  
#Design a program that prompts the user to enter the names of two primary colors to mix.
#If the user enters anything other than “red,” “blue,” or “yellow,” the program should display an error message. Otherwise, the program
# should display the name of the secondary color that results.
colors = ["red", "blue", "yellow"]
print("Let's mix some colors? Red, blue and yellow are the primary colors\nMix two primary colors and find out a secondary color!")
primary_one = input("Enter a primary color: ")
primary_two = input("Enter a primary color: ")
if primary_one and primary_two not in colors:
    print("Plese enter only the primary colors!")
elif primary_one == colors[0] and primary_two == colors[1]:
    print("Purple")
elif primary_one == colors[1] and primary_two == colors[0]:
    print("Purple")
elif primary_one == colors[0] and primary_two == colors[2]:
    print("Orange")
elif primary_one == colors[2] and primary_two == colors[0]:
    print("Orange")
elif primary_one == colors[1] and primary_two == colors[2]:
    print("Green")
elif primary_one == colors[2] and primary_two == colors[1]:
    print("Green")
