#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SyringJ
#
# Created:     11/09/2022
# Copyright:   (c) SyringJ 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def consumables():

    category = 'Blocks'
    choice = 0
    listitem = 1
    inputtype = 0
    total = 0
    repeatcraft = 0
    block_craft = { "Yield" : 10},
    block = []
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
            print("\n", block_craft[block[idx]])
        else:
            print("Please choose one of the given values.") # Error catch to prevent program from crashing due to a mispelled word or someone thinking their smart and trying to break the code
            choice = 0 # Resets the value to 0 so the loop repeats
        while total == 0:
            total = input(f"\nHow many {block[idx]} do you want: ")
            if not total.isalpha(): # Makes sure that the input is a number and not a string.
                total = int(total)
            else:
                total = 0
                print("Thats not a number. Choose a number Numbnuts.")
                continue
            if ((int(total) // block_craft[block[idx]]["Yield"]) == int(total) / block_craft[block[idx]]["Yield"]):
                repeatcraft = (int(total) // block_craft[block[idx]]["Yield"])
            else:
                repeatcraft = (int(total) // block_craft[block[idx]]["Yield"])+1
            #print(type(block_craft[block[idx]]))
            for k,v in (block_craft[block[idx]].items()):
                print(f"\n{k} = {v*repeatcraft}")




