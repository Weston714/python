import time # This is required to include time module.
import shutil #import copytree, ignore_patterns
import os 

#def coppy():
   # shutil.copy("C:\Users\Weston Simon\Downloads\python-main", "C:\Users\Weston Simon\Desktop\testing" + filepath, *, follow_symlinks=True)
markedday = "Wednesday"
weeknumber = int(1)
newmonth = ()
repeat = 0
monthname = "a"
week = "a"
markedday = "a"

while(True):
    #print("Hi")

    #repeat = repeat + 1
    localtime = time.localtime()
    if localtime[4] == 0 or localtime[4] == 24:
    
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

        month = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"} 
        #Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 

        if localtime[2] == 1 and localtime[3] == 1:
            newmonth = int(localtime[1])
            monthname = month[newmonth]
            print("Changing to new " + monthname + " month folder")
            os.mkdir(str("D:/2021/" + monthname))
            weeknumber = 0




        
        if localtime[6] == 6 and localtime[3] == 24:
            weeknumber = weeknumber + 1
            week = "Week" + str(weeknumber)
            os.mkdir(str("D:/2021/" + monthname + "/" + week))




        if day != markedday:
            markedday = day
            #os.mkdir(str("D:/2021/" + monthname + "/" + week + "/" + markedday))
            print("Creating new day forlder")



        filename = str(localtime[3]) + "." + str(localtime[4]) + "." + str(localtime[5]) + " " + day + " " + str(localtime[1]) + "." + str(localtime[2]) + "." + str(localtime[0])
        print(filename)
        #+ day + str(localtime[1]) + "/" + str(localtime[2]) + "/" + str(localtime[0])
        #name = str("C:\Users\Weston Simon\Desktop" + filename)
        #print(filename)
        os.chdir(str("D:/2021/" + monthname + "/" + week + "/" + markedday))
        os.mkdir(str("D:/2021/" + monthname + "/" + week + "/" + markedday + "/" + filename))
        filepath = filename
        #shutil.copytree(src, dst, symlinks = False, ignore = None, copy_function = copy2, igonre_dangling_symlinks = False)
        #shutil.copyfile("C:\Users\Weston Simon\Downloads\python-main", "C:\Users\Weston Simon\Desktop\testing", *, follow_symlinks=True)
        #coppy()
        src ="R:/pack32v3/world"
        dest ="D:/2021/" + monthname + "/" + week + "/" + markedday + "/" + filepath +  "/world"
        file = "session.lock"
        shutil.copytree(src, dest)

    
        #print(source + target)
        #shutil.copy2(source, target)
        #time.sleep(300)
        #if repeat >= 5:
            #break
        time.sleep(60)
        continue
    else:
        print("Waiting 30 seconds and trying again")
        time.sleep(30)
        continue

def _ignore_patterns(path, names):
    keep = set(name for pattern in patterns
    for name in filter(names, pattern))
    ignore = set(name for name in names
    if name not in keep and not isdir(join(path, name)))
    return ignore
    return _ignore_patterns








    
#ticks = time.time()
#print ("Number of ticks since 12:00am, January 1, 1970:", ticks)
