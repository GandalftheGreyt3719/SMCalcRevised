import time
def blocks():


    category = 'Blocks'
    choice = 0
    listitem = 1
    inputtype = 0
    total = 0
    repeatcraft = 0
    block_craft = {"Concrete 1": {"Scrap Stone" : 5, "Water" : 5, "Chemical" : 5, "Yield" : 10}, "Concrete 2":{"Concrete 1" : 15, "Metal 1" : 2, "Yield" : 10},"Concrete 3" : {"Concrete 2" : 15, "Metal 2" : 2, "Yield" : 10}, "Wood 1" : {"Scrap Wood" : 15, "Yield" : 10},"Wood 2" : {"Wood 1" : 15,"Metal 1" : 1, "Yield" : 10},"Wood 3" : {"Wood 2" :15, "Metal 2" : 1, "Yield" : 10},"Metal 1" : {"Scrap Metal" : 15, "Yield" : 10},"Metal 2" : {"Metal 1" : 15, "Ember" : 1, "Water" : 2, "Yield" : 10},"Metal 3" : {"Metal 2" : 20, "Ember" : 2, "Water" : 4, "Yield" : 10},"Barrier Block" : {"Wood 1" : 10, "Paint Ammo" :1, "Yield" : 10 },"Extruded Metal" : {"Metal 1":5, "Yield":10},"Tile Block" : {"Scrap Stone":10, "Paint Ammo":1, "Yield":10},"Brick Block" : {"Scrap Stone" : 10, "Yield":10 },"Glass Block" : {"Sand" : 10, "Ember" : 1, "Yield":10},"Glass Tile" : {"Sand" : 10, "Ember" : 1, "Yield":10},"Path Light" : {"Metal 1" : 10, "Circut Board" : 1, "Yield":10},"Cardboard" : {"Scrap Wood" :5, "Yield":20},"Bubble Plastic" : {"Crude Oil" : 5, "Yield":10},"Carpet" : {"Cotton" : 5, "Paint Ammo": 1, "Yield":10},"Net Block" : {"Metal 1" : 2, "Yield":10},"Solid Net" : {"Metal 1" : 5, "Yield":10},"Punched Steel" : {"Metal 1":5, "Yield":10},"Restroom Block" : {"Scrap Stone":10,"Bees Wax":1, "Yield":10},"Diamond Plate" : {"Metal 1": 10, "Yield":10},"Sand" : {"Scrap Stone":5, "Yield":10},"Armored Glass" : {"Glass":10,"Net Block":2,"Ember":1, "Yield":10 }}
    block = ["Concrete 1","Concrete 2","Concrete 3","Wood 1","Wood 2","Wood 3","Metal 1","Metal 2","Metal 3","Barrier Block","Extruded Metal","Tile Block","Brick Block","Glass Block","Glass Tile","Path Light","Cardboard","Bubble Plastic","Carpet","Net Block","Solid Net","Punched Steel","Restroom Block","Diamond Plate","Sand","Armored Glass"]
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
blocks()

