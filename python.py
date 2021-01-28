""" 
Weston Simon
1/28/21
combo menue
"""
Sandwich = input("Do you want a Sandwich? ")
if Sandwich == "Yes":
    Sandwich_type = input("What type of sandwich do you want? ")
elif Sandwich == "No":
    Sandwich_type == "None"

if Sandwich_type == "Chicken":
    print("Chicen $5.25")
    meal_price = float(5.25)

elif Sandwich_type == "Beef":
    print("Beef $6.25")
    meal_price = float(6.25)

elif Sandwich_type == "Tofu":
    print("Tofu $5.25")
    meal_price = float(5.25)
elif Sandwich_type == "None":
    meal_price = float(0)

else:
    print("invalid sandwich selection please restart the program and try again with one of the three sandwich types: Chicken, Beef, Tofu")

    

Drink = input("Would you like a drink? ")

if Drink == "No":
    print("No drink selected proceding to checkout ")
    DrinkSize = str("None")

elif Drink == "Yes":
    DrinkSize = input("What size drink would you like? ")

if DrinkSize == "Small":
    print("Small $1.00")
    DrinkPrice = float(1.00)

elif DrinkSize == "Medium":
    print("Medium $1.75")
    DrinkPrice = float(1.75)

elif DrinkSize == "Large":
    print("Large $2.25")
    DrinkPrice = float(1.75)

elif DrinkSize == ("None"):
    DrinkPrice = float(0)

Fries = input("Would you like French Fries? ")

if Fries == "Yes":
    FriesSize = input("What size of French Fries do you want? ")
elif Fries == "No":
    print("No fries sellected proceding to checkout.")
    FriesSize = str("none")

if FriesSize == "Small":
    print("Small fries $1.00")
    FriesPrice = float(1.00)
    MegaFries = input("Would you like to mega size your Fries? ")
    if MegaFries == "Yes":
        FriesPrice = float(2.00)

elif FriesSize == "Medium":
    print("Medium Fries: $1.50")
    FriesPrice = float(1.50)

elif FriesSize == "Large":
    print("Large Fries: $2.00")
    FriesPrice = float(2.00)
elif FriesSize == "none":
    FriesPrice = float(0) 

Ketchup = int(input("How many ketchup packets would you like?"))
TotalKetchup = float(Ketchup * 0.25)

if Sandwich == Drink == Fries == "Yes":
    print("You recive our $1.00 discount for ordering a sandwich with fries and a drink.")
    Discount = float(1.00)
    DiscountRecived = (True)
else:
    Discount = float(0)
    DiscountRecived = (False)

Items = (Sandwich_type + DrinkSize + FriesSize + Ketchup)
print(Items)

Checkout = float(meal_price + DrinkPrice + FriesPrice + TotalKetchup)
print("Total= $"+str(Checkout))