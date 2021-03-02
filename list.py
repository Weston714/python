""" 
Weston Simon
1/28/21
combo menu list
"""
Selections = ["","","",]
Items = ["", 0.0, "", 0.0, "", 0.0]
print("Menu:\n Sandwiches: chicken $5.25, beef $6.25, tofu $5.75\n Drinks: small $1.00 medium $1.75 large $2.25\n Fries: small $1.00(Mega size: $2.00) medium $1.50 large $2.00\n Ketchup: $0.25 per packet\n Combo discont $1.00 if you buy a sandwich fries and a drink.\n All selections Must be answered with:\n Yes/No Small,Medium,Large")
while(True):
    restart = (False)
    #When the customer inputs an invalid order it restarts that part of the order

    Sandwich = input("Do you want a Sandwich? ")
    Sandwich = Sandwich.lower()
    
    if Sandwich == "yes":
        Selections[0] = 'Yes'
        Sandwich_type = input("What type of sandwich do you want? ")
        Sandwich_type = Sandwich_type.lower()
    
    elif Sandwich == "no":
        Selections[0] = 'No'
        Sandwich_type = "None"
        print("No sandwich selected")
    #Asks if the coustomer wants a sandwich

    if Sandwich_type == "chicken":
        print("Chicken $5.25")
        Items[0] = "Chicken"
        Items[1] = float(5.25)
        #meal_price = float(5.25)
    #Chicken sandwich option
    elif Sandwich_type == "beef":
        print("Beef $6.25")
        Items[0] = "Beef"
        Items[1] = float(6.25)
        #meal_price = float(6.25)
    #Beef sandwich option
    elif Sandwich_type == "tofu":
        print("Tofu $5.25")
        Items[0] = "Tofu"
        Items[1] = float(6.25)
        #meal_price = float(5.25)
    #Tofu sandwich option
    elif Sandwich_type == "None":
        #meal_price = float(0)
        Items[0] = "None"
        Items[1] = float(0.0)
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
        #DrinkSize = str("None")
        Items[2] = "None"
        Items[3] = float(0.0)
        Selections[1] = 'No'
   
    elif Drink == "yes":
        Selections[1] = 'Yes'
        DrinkSize = input("What size drink would you like? ") 
        DrinkSize = DrinkSize.lower()
    #prosecesses if the coustomer wants a drink
    if DrinkSize == "small":
        print("Small $1.00")
        Items[2] = "Small"
        Items[3] = float(1.00)
        #DrinkPrice = float(1.00)
    #drink size small
    elif DrinkSize == "medium":
        print("Medium $1.75")
        Items[2] = "Medium"
        Items[3] = float(1.75)
        #DrinkPrice = float(1.75)
    #drink size medium
    elif DrinkSize == "large":
        print("Large $2.25")
        Items[2] = "Large"
        Items[3] = float(2.25)
        #DrinkPrice = float(2.25)
    #drink size large
    elif DrinkSize == ("None"):
        Items[2] = "None"
        Items[3] = float(0.0)
        #DrinkPrice = float(0)
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
        Selections[2] = 'Yes'
        FriesSize = input("What size of French Fries do you want? ")
        #FriesSize = FriesSize.lower()
    
    elif Fries == "no":
        Selections[2] = 'No'
        print("No fries selected")
        FriesSize = str("none")
        Items[4] = "None"
        Items[5] = float(0.0)
    #Prosesses the response for if the coustomer wants fries
    if FriesSize == "Small":
        print("Small fries $1.00")
        #FriesPrice = float(1.00)
        Items[4] = "Small"
        Items[5] = float(1.00)
        MegaFries = input("Would you like to mega size your Fries? ")
        #fries size small
        if MegaFries == "Yes":
            #FriesPrice = float(2.00)
            #FriesSize = ("MEGA")
            Items[4] = "MEGA"
            Items[5] = float(2.00)
        #if they want mega fries
    elif FriesSize == "Medium":
        print("Medium Fries: $1.50")
        Items[4] = "Medium"
        Items[5] = float(1.50)
        #FriesPrice = float(1.50)
        #fries size medium
    elif FriesSize == "Large":
        print("Large Fries: $2.00")
        Items[4] = "Large"
        Items[5] = float(2.00)
        #FriesPrice = float(2.00)
        #fries size large
    elif FriesSize == "none":
        Items[4] = "None"
        Items[5] = float(0.0)
        #FriesPrice = float(0) 
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
print(Selections)
Ketchup = int(input("How many ketchup packets would you like? "))
TotalKetchup = float(Ketchup * 0.25)
#ask if the coustomer wants ketchup and calcualtes the price 
if Selections == ['Yes', 'Yes', 'Yes']:
    print("You recive our $1.00 discount for ordering a sandwich with fries and a drink.")
    Discount = float(-1.00)
    DiscountRecived = (True)
    print("Recived")
    
else:
    Discount = float(0)
    DiscountRecived = (False)
    #To tell if the discount will be aplied or not
    print("Not")
#print(Items)
Items_T = str("Sandwich: " + Items[0] + "   Drink: " + Items[2] + "   Fries: " + Items[4] + "    Number of ketchup packets: " +str(Ketchup))
print(Items_T)
#list all of the items selected
Checkout = float(Items[1] + Items[3] + Items[5] + TotalKetchup + Discount)
checkout_formatted = "{:.2f}".format(Checkout)
print("Total= $" + str(checkout_formatted))
#Calculates the total of the order