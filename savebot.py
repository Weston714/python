import time # This is required to include time module.
import shutil
import os 


repeat = 0
while(True):
    print("Hi")
    time.sleep(5)
    repeat = repeat + 1
    localtime = time.localtime()
    print(localtime[3])
    #os.mkdir("data")
    #shutil.copytree(src, dst, symlinks = False, ignore = None, copy_function = copy2, igonre_dangling_symlinks = False)


    if repeat >= 5:
        break
    continue











#ticks = time.time()
#print ("Number of ticks since 12:00am, January 1, 1970:", ticks)
