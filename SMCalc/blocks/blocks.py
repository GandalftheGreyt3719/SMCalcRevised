#-------------------------------------------------------------------------------
# Name:        blocks
# Purpose:
#
# Author:      jackson syring
#
# Created:     07/09/2022
# Copyright:   (c) jackson syring 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time
def blocks():


    category = 'Blocks'
    bulkcraft = 1
    choice = 0
    listitem = 1
    inputtype = 0
    block = ["Concrete_1","Concrete_2","Concrete_3","Wood_1","Wood_2","Wood_3","Metal_1","Metal_2","Metal_3","Barrier_Block","Extruded_Metal","Tile_Block","Brick_Block","Glass_Block","Glass_Tile","Path_Light","Cardboard","Bubble_Plastic","Carpet","Net_Block","Solid_Net","Punched_Steel","Restroom_Block","Diamond_Plate","Sand","Armored_Glass"]
    for x in block:
        print(listitem, x)

        listitem += 1
        time.sleep(0.125)
    while choice == 0:
        choice = input("Choose a block (Enter only the Number):")
        if not choice.isalpha(): # Makes sure that the input is a number and not a string.
            choice = int(choice)
        else:
            choice = 0
            print("Thats not a number. Choose a number Numbnuts.")
        if choice in range (1,26+1): # reduces the if elif else chunk to a single if else statement. 26+1 allows 26 to be a value given, while allowing past the choice-1
            idx = choice - 1
            print("\n", block[idx])
        else:
            print("Please choose one of the given values.") # Error catch to prevent program from crashing due to a mispelled word or someone thinking their smart and trying to break the code
            choice = 0 # Resets the value to 0 so the loop repeats