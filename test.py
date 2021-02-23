#Combo_menu_logan_v1#
sandwitch = int(input("Welcome to King Burger, what may I get for you today? (1)Chicken Sandwich: $5.25, (2)Beef Sandwich: $6.25, or (3)Tofu Sandwich: $5.75"))
total = 0
#This part of the code makes an input of what sandwitch the customer will choose.#
if(sandwitch == 1):
  print(" ")
  print("You would like the Chicken Sandwich?")
  sandwitch_type = int(input("(1)Yes or (0)No"))
 
#For sandwitch 1, 2, and 3 the if statement is making a scenario of the customer choosing a certain sandwitch and the person confirming that they wanted.#  
  if(sandwitch_type == 1):
    print(" ")
    total = total + 5.25
    Sandwich_Meat = ("Chicken")
#If the answer is yes then add $5.25 to the total cost.#    
  if(sandwitch_type == 0):
    print(" ")
    sandwitch = int(input("(2)Beef Sandwich: $6.25, or (3)Tofu Sandwich: $5.75"))
#If the answer is no then ask what else they would like.#    
#This same concept is used throughout each selection of sandwitch    
if(sandwitch == 2):
  print(" ")
  print("You would like the Beef Sandwich?")
  sandwitch_type = int(input("(1)Yes or (0)No"))
 
   
  if (sandwitch_type == 1):
    print(" ")
    total = total + 6.25
    Sandwich_Meat = ("Beef")
 
  if(sandwitch_type == 0):
    print(" ")
    sandwitch = int(input("(1)Chicken Sandwich: $5.25, or (3)Tofu Sandwich: $5.75"))

if(sandwitch == 3):
  print(" ")
  print("You would like the Tofu Sandwich?")
  sandwitch_type = int(input("(1)Yes or (0)No"))
 
 
  if (sandwitch_type == 1):
    print(" ")
    total = total + 5.75
    Sandwich_Meat = ("Tofu")
   
  if(sandwitch_type == 0):
    print(" ")
    sandwitch = int(input("(1)Chicken Sandwich: $5.25, or (2)Beef Sandwich: $6.25"))
#Combo_menu_logan_v2#
drink = int(input("Would you like a (1)Small: $1.00, (2)Medium: $1.75, or (3)Large: $2.25 drink?"))  
 
if(drink == 1):
    print(" ")
    print("Would you like a small?")
    drink_size = int(input("(1)Yes or (0)No"))
    Drink_Cup = ("Small")
   
    if(drink_size == 1):
      print(" ")
      total = total + 1.00  

    if(drink_size == 0):
      print(" ")
      drink = int(input("Would you like a (2)Medium: $1.75, or (3)Large: $2.25"))  

if(drink == 2):
    print(" ")
    print("Would you like a medium?")
    drink_size = int(input("(1)Yes or (0)No"))
    Drink_Cup = ("Medium")

    if(drink_size == 1):
      print(" ")
      total = total + 1.75
   
    if(drink_size == 0):
      print(" ")
      drink = int(input("Would you like a (1)Small: $1.00, or (3)Large: $2.25"))
   
if(drink == 3):
    print(" ")
    print("Would you like a large?")
    drink_size = int(input("(1)Yes or (0)No"))
    Drink_Cup = ("Large")

    if(drink_size == 1):
      print(" ")
      total = total + 2.25
   
    if(drink_size == 0):
      print(" ")
      drink = int(input("Would you like a (1)Small: $1.00, or (2)Medium: $1.75?"))
#Combo_menu_logan_v3#  
fries = int(input("Would you like (1)Small: $1.00, (2)Medium: $1.50, or (3)Large: $2.00 french fries?"))  
 
if(fries == 1):
    print(" ")
    print("Would you like a small?")
    fries_size = int(input("(1)Yes or (0)No"))
    Fries_Box = ("Small")
   
    if(fries_size == 1):
      print(" ")
      print("Would you like to try our jumbo size?")
      fries_size = int(input("(1)Yes or (0)No"))
     
      if(fries_size == 1):
        print("")
        total = total + 2.00
        Fries_Box = ("Jumbo")
     
      if(fries_size == 0):
        print("")
        total = total + 1.00
#The task was that if the customer wanted small fries, then they were offered jumbo fries.#    
    if(fries_size == 0):
      print(" ")
      fries = int(input("Would you like a (1)Small: $1.00, (2)Medium: $1.75, or (3)Large: $2.25"))  

if(fries == 2):
    print(" ")
    print("Would you like a medium?")
    fries_size = int(input("(1)Yes or (0)No"))
    Fries_Box = ("Medium")
   
    if(fries_size == 1):
      print(" ")
      total = total + 1.75
   
    if(fries_size == 0):
      print(" ")
      fries = int(input("Would you like a (1)Small: $1.00, (2)Medium: $1.75, or (3)Large: $2.25"))
     
if(fries == 3):
    print(" ")
    print("would you like a large?")
    fries_size = int(input("(1)Yes or (0)No"))
    Fries_Box = ("Large")
   
    if(fries_size == 1):
      print(" ")
      total = total + 2.00
   
    if(fries_size == 0):
      print(" ")
      drink = int(input("Would you like a (1)Small: $1.00, (2)Medium: $1.75, or (3)Large: $2.25"))
#Combo_menu_logan_v4#
ketchup = int(input("How many ketchup packets would you like?"))
total = total + (ketchup * 0.25)
if (fries_size == sandwitch_type == drink_size == 1):
   total = total - 1.00
#This will make the discount.#
print(str("Sandwich: " + str(Sandwich_Meat) + " \nDrink: " + str(Drink_Cup) + " \nFries: " + str(Fries_Box) + " \nNumber of ketchup packets: " + str(ketchup)))
#print("")
total = "{:.2f}".format(total)
print("$" + str(total))
#This will ask the customer how many ketchup packets they would like then display the total price!!#



