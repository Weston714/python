import time # This is required to include time module.
import shutil
import os 


repeat = 0
while(True):
    print("Hi")
    #time.sleep(5)
    repeat = repeat + 1
    localtime = time.localtime()
    if localtime[6] == 0:
        day = "Monday"
    elif localtime[6] == 1:
        day = "Tuesday"
    elif localtime[6] == 2:
        day = "Wednesday"
    elif localtime[6] == 3:
        day = "Thrusday"
    elif localtime[6] == 4:
        day = "Friday"
    elif localtime[6] == 5:
        day = "Saturday"
    elif localtime[6] == 6:
        day = "Sunday"


    filename = ("Time" + str(localtime[3]) + ":" + str(localtime[4]) + ":" + str(localtime[5]) + " Date " + day + " " + str(localtime[1]) + "/" + str(localtime[2]) + "/" + str(localtime[0]) + " Julian day " + str(localtime[7]))
    print(filename)
    
    name = str(filename)
    os.mkdir(name)
    #shutil.copytree(src, dst, symlinks = False, ignore = None, copy_function = copy2, igonre_dangling_symlinks = False)


    break











#ticks = time.time()
#print ("Number of ticks since 12:00am, January 1, 1970:", ticks)
