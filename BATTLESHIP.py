#Nicholas Honton
#AI Program #3

#Default board - 10 x 10
#Alternate sizes - 12, 15, 20?
# PvP
# Player vs AI - Easy, Hard, EX Hard
# AI vs AI
# Help Menu
# Different Pieces
# Nuclear Option

def Help(): # help menu
	select = "R"
	#add a while loop
	while select != "X":
		print("Enter 'M' to see different game modes")
		print("Enter 'O' to see game options")
		print("Enter 'X' to exit back to main menu")
		select = input("")
		if select in ('M','m')
			Modes()
		if (select in ("O","o")
			Options()
	pass
	
def Modes(): # help submenu
	print("Mode 1: Player vs Player")
	print("Mode 2: Player vs AI (Easy)")
	print("Mode 3: Player vs AI (Hard)")
	print("Mode 4: Player vs AI (EX Hard)")
	print("!!! - Warning - Mode 4 Not Recommended")
	print("Mode 5: AI vs AI")
	pass

def Options(): # help submenu
	print("Board Sizes: 1 for 10x10")
	print("             2 for 12x12")
	print("             3 for 15x15")
	print("             4 for 20x20")
	print("New Ships: 1 to include")
	print("           2 to exclude")
	print("Nuclear Option: 1 to exclude")
	print("                2 for MAD Mode")
	print("                3 for All-Out Mode")
	pass
	

print("WELCOME TO BATTLEBOT 3K")
Help()