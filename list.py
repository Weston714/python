""" 
Weston Simon
1/28/21
combo menu list
"""
print("Menu:\n Sandwiches: chicken $5.25, beef $6.25, tofu $5.75\n Drinks: small $1.00 medium $1.75 large $2.25\n Fries: small $1.00(Mega size: $2.00) medium $1.50 large $2.00\n Ketchup: $0.25 per packet\n Combo discont $1.00 if you buy a sandwich fries and a drink.\n All selections Must be answered with:\n Yes/No Small,Medium,Large")
while(True):
    restart = (False)
    #When the customer inputs an invalid order it restarts that part of the order

    Sandwich = input("Do you want a Sandwich? ")
    Sandwich = Sandwich.lower()
    
    if Sandwich == "yes":
        Sandwich_type = input("What type of sandwich do you want? ")
        Sandwich_type = Sandwich_type.lower()
    
    elif Sandwich == "no":
        Sandwich_type = "None"
        print("No sandwich selected")
    #Asks if the coustomer wants a sandwich

    if Sandwich_type == "chicken":
        print("Chicken $5.25")
        meal_price = float(5.25)
    #Chicken sandwich option
    elif Sandwich_type == "beef":
        print("Beef $6.25")
        meal_price = float(6.25)
    #Beef sandwich option
    elif Sandwich_type == "tofu":
        print("Tofu $5.25")
        meal_price = float(5.25)
    #Tofu sandwich option
    elif Sandwich_type == "None":
        meal_price = float(0)
    #If the coustomer dosn't want a sandwich
    else:
        print("invalid sandwich selection please select one of the three sandwich types: Chicken, Beef, Tofu")
        restart = (True)
    #When the customer inputs an invalid order it restarts that part of the order
    if (restart == True):
        continue
    else:
        break
    #When the customer inputs an invalid order it restarts that part of the order
    #End of sandwich order

while(True):       
    restart = (False)
    #When the customer inputs an invalid order it restarts that part of the order

    Drink = input("Would you like a drink? ")
    Drink = Drink.lower()
    #ask coustomer if they want a drink

    if Drink == "no":
        print("No drink selected")
        DrinkSize = str("None")
   
    elif Drink == "yes":
        DrinkSize = input("What size drink would you like? ") 
        DrinkSize = DrinkSize.lower()
    #prosecesses if the coustomer wants a drink
    if DrinkSize == "small":
        print("Small $1.00")
        DrinkPrice = float(1.00)
    #drink size small
    elif DrinkSize == "medium":
        print("Medium $1.75")
        DrinkPrice = float(1.75)
    #drink size medium
    elif DrinkSize == "large":
        print("Large $2.25")
        DrinkPrice = float(2.25)
    #drink size large
    elif DrinkSize == ("None"):
        DrinkPrice = float(0)
    #If the coustomer dosn't want a drink
    else:
        print("Invalid drink option please enter a valid drink option")
        restart = True
    #When the customer inputs an invalid order it restarts that part of the order
    if (restart == True):
        continue
    else:
        break
    #When the customer inputs an invalid order it restarts that part of the order

while(True):
    restart = (False)
    #When the customer inputs an invalid order it restarts that part of the order
    Fries = input("Would you like French Fries? ")
    Fries = Fries.lower()
    #ask if the coustomer wants fries
    if Fries == "yes":
        FriesSize = input("What size of French Fries do you want? ")
        #FriesSize = FriesSize.lower()
    
    elif Fries == "no":
        print("No fries selected")
        FriesSize = str("none")
    #Prosesses the response for if the coustomer wants fries
    if FriesSize == "Small":
        print("Small fries $1.00")
        FriesPrice = float(1.00)
        MegaFries = input("Would you like to mega size your Fries? ")
        #fries size small
        if MegaFries == "Yes":
            FriesPrice = float(2.00)
            FriesSize = ("MEGA")
        #if they want mega fries
    elif FriesSize == "Medium":
        print("Medium Fries: $1.50")
        FriesPrice = float(1.50)
        #fries size medium
    elif FriesSize == "Large":
        print("Large Fries: $2.00")
        FriesPrice = float(2.00)
        #fries size large
    elif FriesSize == "none":
        FriesPrice = float(0) 
        #if the coustomer dosen't want fries
    else:
        print("Invalid fries option please inter a valid option")
        restart = (True)
         #When the customer inputs an invalid order it restarts that part of the order  
    if (restart == True):
        continue
    else:
        break
     #When the customer inputs an invalid order it restarts that part of the order

Ketchup = int(input("How many ketchup packets would you like? "))
TotalKetchup = float(Ketchup * 0.25)
#ask if the coustomer wants ketchup and calcualtes the price 
if Sandwich == Drink == Fries == "Yes":
    print("You recive our $1.00 discount for ordering a sandwich with fries and a drink.")
    Discount = float(-1.00)
    DiscountRecived = (True)
    
else:
    Discount = float(0)
    DiscountRecived = (False)
    #To tell if the discount will be aplied or not
Items = str("Sandwich: " + Sandwich_type + "   Drink: " + DrinkSize + "   Fries: " + FriesSize + "    Number of ketchup packets: " +str(Ketchup))
print(Items)
#list all of the items selected
Checkout = float(meal_price + DrinkPrice + FriesPrice + TotalKetchup + Discount)
checkout_formatted = "{:.2f}".format(Checkout)
print("Total= $" + str(checkout_formatted))
#Calculates the total of the order