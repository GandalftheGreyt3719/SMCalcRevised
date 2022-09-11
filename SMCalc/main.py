#-------------------------------------------------------------------------------
# Name:        main
# Purpose:      this is the interface for the
#
# Author:      SyringJ
#
# Created:     09/09/2022
# Copyright:   (c) SyringJ 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time, clearscreen
from blocks import blocks
#from interactiveparts import interactive
#from parts import parts
#from tools import tools
#from consumables import consumables
category = 0
categories = ["Blocks","Tools","Parts","Interactive Parts","Consumables"]
listitem =1
clearscreen.clearscreen()
for x in categories:
    print(listitem,x)
    listitem += 1
while category == 0:
    category = input("Choose a category (Use the Number only)")
    if not category.isalpha(): # Makes sure that the input is a number and not a string.
        category = int(category)
    else:
        category = 0
        continue
        print("Thats not a number. Choose a number Numbnuts.")
    if category in range (1,5+1): # reduces the if elif else chunk to a single if else statement. 5+1 allows 5 to be a value given, while allowing past the category-1
        idx = category - 1
        print("\n", categories[idx])

        if idx == 0:
            clearscreen.clearscreen()
            blocks()
        elif idx == 1:
            clearscreen.clearscreen()
            tools()
        elif idx == 2:
            clearscreen.clearscreen()
            parts()
        elif idx == 3:
            clearscreen.clearscreen()
            interactive()
        elif idx == 4:
            clearscreen.clearscreen()
            consumables()
    else:
            print("Thats not a valid option")
            category = 0

