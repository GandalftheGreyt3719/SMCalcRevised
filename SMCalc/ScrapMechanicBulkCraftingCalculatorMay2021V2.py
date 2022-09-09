#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  s.py
#
#  Copyright 2021 GandalfTheGreytGamer3791 <Jaxer6563@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


"""
This is a Calculator that will help in crafting Blocks, Interactive Parts, Consumables, and Parts in bulk.
When prompted, choose from a list of parts, and then input the amount needed.
As a simple example, We will use the Glowstick crafting.
1st, the program will ask for how much you want.
2nd, then it will multiply the value by the already known values. In the case of glowsticks, at 32 glowsticks, it will be 32 glow, 32 chemical, and 3-ish minutes.

"""
import time, clearscreen
#from parts import parts
from blocks import blocks
#from tools import tools
#from consumables import consumables
#from interactiveparts import interactive

bulkcraft = 1
category = False


while category == False:
	choice = input("Are you crafting Parts, Blocks, Tools, Consumables, or Interactive Parts?\n[Please use same Capitalization and spaces] \n ")
	if choice == "Parts":
		clearscreen.clearscreen()
		parts()
		category = True
	elif choice == "Blocks":
		clearscreen.clearscreen()
		blocks()
		category = True
	elif choice == "Tools":
		clearscreen.clearscreen()
		tools()
		category = True
	elif choice == "Consumables":
		clearscreen.clearscreen()
		consumables()
		category = True
	elif choice == "Interactive Parts":
		clearscreen.clearscreen()
		interactive()
		category = True

    else:
        print("Choose a category Numbnuts")
        category = False
