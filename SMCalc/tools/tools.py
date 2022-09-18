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
import time
def tools():

    category = 'tools'
    choice = 0
    listitem = 1
    inputtype = 0
    total = 0
    repeatcraft = 0
    block_craft = {"Weld_Tool":{"Metal 2" : 20, "Ciruit Board" :5, "Component Kit" : 5}, "Paint_Tool":{"Metal 1":10,"Glass":5,"Component Kit":1},"Connect_Tool":{"Scrap Metal":10,"Circuit Board":2}}
    block = ["Weld_Tool", "Paint_Tool", "Connect_Tool"]
    for x in block:
        print(listitem, x)

        listitem += 1
        time.sleep(0.125)
    while choice == 0:
        choice = input("Choose a tool (Enter only the Number):")
        if not choice.isalpha(): # Makes sure that the input is a number and not a string.
            choice = int(choice)
        else:
            choice = 0
            print("Thats not a number. Choose a number Numbnuts.")
        if choice in range (1,3+1): # reduces the if elif else chunk to a single if else statement. 26+1 allows 26 to be a value given, while allowing past the choice-1
            idx = choice - 1
            print("\n", block[idx])
        else:
            print("Please choose one of the given values.") # Error catch to prevent program from crashing due to a mispelled word or someone thinking their smart and trying to break the code
            choice = 0 # Resets the value to 0 so the loop repeats
            continue
        while total == 0:
            repeatcraft = 1
            for k,v in (block_craft[block[idx]].items()):
                print(f"\n{k} = {v*repeatcraft}")
            total =1





