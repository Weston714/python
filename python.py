""" 
Weston Simon
1/28/21
combo menue
"""

Sandwich_type = input("What type of sandwich do you want? ")

if Sandwich_type == "Chicken":
    print("Chicen $5.25")
    meal_price = float(5.25)

elif Sandwich_type == "Beef":
    print("Beef $6.25")
    meal_price = float(6.25)

elif Sandwich_type == "Tofu":
    print("Tofu $5.25")
    meal_price = float(5.25)

else:
    print("invalid sandwich selection please restart the program and try again with one of the three sandwich types: Chicken, Beef, Tofu")

    

Drink = input("Would you like a drink? ")

if Drink == "No":
    print("No drink selected proceding to checkout ")
    DrinkPrice = int(0)

elif Drink == "Yes":
    DrinkSize = input("What size drink would you like? ")

    