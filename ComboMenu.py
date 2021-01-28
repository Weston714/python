""" 
Weston Simon
1/28/21
combo menu
"""

while(True):
    restart = (False)
    #When the customer inputs an invalid order it restarts that part of the order

    Sandwich = input("Do you want a Sandwich? ")
    if Sandwich == "Yes":
        Sandwich_type = input("What type of sandwich do you want? ")
    
    elif Sandwich == "No":
        Sandwich_type == "None"
    #Asks if the coustomer wants a sandwich

    if Sandwich_type == "Chicken":
        print("Chicen $5.25")
        meal_price = float(5.25)
    #Chicken sandwich option
    elif Sandwich_type == "Beef":
        print("Beef $6.25")
        meal_price = float(6.25)
    #Beef sandwich option
    elif Sandwich_type == "Tofu":
        print("Tofu $5.25")
        meal_price = float(5.25)
    #Tofu sandwich option
    elif Sandwich_type == "None":
        meal_price = float(0)
    #If the coustomer dosn't want a sandwich
    else:
        print("invalid sandwich selection please restart the program and try again with one of the three sandwich types: Chicken, Beef, Tofu")
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
    #ask coustomer if they want a drink

    if Drink == "No":
        print("No drink selected preceding to checkout ")
        DrinkSize = str("None")
   
    elif Drink == "Yes":
        DrinkSize = input("What size drink would you like? ")    
    #prosecesses if the coustomer wants a drink
    if DrinkSize == "Small":
        print("Small $1.00")
        DrinkPrice = float(1.00)
    #drink size small
    elif DrinkSize == "Medium":
        print("Medium $1.75")
        DrinkPrice = float(1.75)
    #drink size medium
    elif DrinkSize == "Large":
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
    #ask if the coustomer wants fries
    if Fries == "Yes":
        FriesSize = input("What size of French Fries do you want? ")
    
    elif Fries == "No":
        print("No fries selected preceding to checkout.")
        FriesSize = str("none")
    #Prosesses the response for if the coustomer wants fries
    if FriesSize == "Small":
        print("Small fries $1.00")
        FriesPrice = float(1.00)
        MegaFries = input("Would you like to mega size your Fries? ")
        #fries size small
        if MegaFries == "Yes":
            FriesPrice = float(2.00)
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
print("Total= $"+str(Checkout))
#Calculates the total of the order