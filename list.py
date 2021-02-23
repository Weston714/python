from colorama import Fore, Back, Style
"""
Weston Simon
2/23/21
List
learning how to control a list
"""

my_classes = ["Computer Science","PE","English 2","Algbra 2","Spanish 1","Bioligy 1","Human Geography"]

print(Fore.GREEN + str(my_classes))

print(Fore.BLUE + "The third class in my list is: " + str(my_classes[2]))

my_classes.append("Prime Time")

print(Fore.RED + str(my_classes))

