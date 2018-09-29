# Nicholas Honton
# Copyright 2018
# originally written 2016 for UA AI course
# Please refer to licensing information on Github

# TODO:
# implement Player vs Player
# implement MAD Mode and All-Out Mode
# more test games vs the AI

# functions:
# starting help menu
def Help():
	select = "R"
	while not (select == "X" or select == "x"):
		print("Enter 'O' to see game options")
		print("Enter 'M' to see different game modes")
		print("Enter 'X' to exit back to main menu")
		select = input("")
		if select in ("M","m"):
			Modes()
		if select in ("O","o"):
			Options()
	pass
	
# help submenu: explanation of game modes
def Modes():
	print("Mode 1: Player vs AI (Easy)")
	print("Mode 2: Player vs AI (Hard)")
	print("Mode 3: Player vs AI (EX Hard)")
	print("!!! - Warning - EX Hard Not Advised - !!!")
	print("Mode 4: Player vs Player")
	pass

# help submenu: explanation of game options
def Options():
	print("Nuclear Option: 1 to exclude")
	print("                2 for MAD Mode")
	print("                3 for All-Out Mode")
	print("                4 for Absolute Terror Field")
	pass
	
# modes submenu: explanation of Easy Mode
def PvA1(): 
	print("")
	print("You have selected Easy Mode")
	print("Here, the AI will just throw out completely random moves each turn")
	print("")
	pass
	
# modes submenu: explanation of Hard Mode
def PvA2():
	print("")
	print("You have selected Hard Mode")
	print("Here, using past data and efficient logic, ")
	print("the AI will try its very hardest to destroy you.")
	print("")
	pass
	
# modes submenu: explanation of EX Hard Mode
def PvA3():
	print("")
	print("You have selected EX Hard Mode")
	print("Another level of difficulty is added by allowing the AI")
	print("to cheat on you if things aren't going its way.")
	print("Like playing with a sibling, but somehow worse.")
	print("")
	pass
	
# options submenu: explanation of MAD Mode
def MUTUALLY_ASSURED():
	print("")
	print("You have selected: Mutually Assured Destruction (MAD) Mode.")
	print("When a winner is declared, their opponent has one final")
	print("superpowered nuclear device to use. If this final strike")
	print("successfully annihilates the enemy, the game is a draw.")
	print("")
	pass
	
# options submenu: explanation of All-Out Mode
def ALL_OUT():
	print("")
	print("You have selected: All-Out Mode.")
	print("Both sides use more powerful missiles")
	print("that can annihilate a 3x3 area in an instant.")
	print("Strike with wild abandon and destroy your foe!")
	print("")
	pass
	
# options submenu: explanation of Absolute Terror Field
# special thank you to Hideaki Anno, director of Neon Genesis Evangelion
# from whom I am lovingly stealing the name for this option
def ATF():
	print("")
	print("Welcome to ABSOLUTE TERROR FIELD")
	print("In this mode, your opponent is mercilessly well-equipped")
	print("with armaments that will crush you in ten turns or less.")
	print("See just how much damage you can do before then!")
	print("")
	pass
	
# Player class and associated functions
class Player:
	# array A keeps track of all spaces where the player has attacked
	A = [[' ' for m in range(10)] for n in range(10)]
	# array B keeps track of where the player's ships have been placed
	B = [[' ' for x in range(10)] for y in range(10)]
	# Types - the names of each kind of vessel
	Types = ["DESTROYER", "SUBMARINE","CRUISER","BATTLESHIP","CARRIER"]
	# Sizes - how many spaces long each vessel is
	# Destroyer is 2, Battleship is 4, etc
	Sizes = 2, 3, 3, 4, 5
	Ships = []
	# Range - each player shot hits this many by this many spaces
	range = 1
	# Place - Player strategically aligns their vessels across the playing field
	def Place(self):
		Instructions() # instruct players how to proceed
		s = 0 # loop counter
		qs = [] # for EX Hard Mode
		while s < 5: # loop to place all ships
			print("Please select where to place", end=" ")
			print(self.Types[s], end=", ")
			print("Size of", end=" ") 
			print(self.Sizes[s]) # asks where to place each ship in turn and provides their size
			i = input("> ") # asks for input
			O = i[0] # single character provides whether the ship is vertical or horizontal
			SZ = self.Sizes[s] # size of the current ship
			P = i[2:] 
			P = PointToPair(P) # P - coordinate provided by player as to where ship should go
			if Check(self.B, O, SZ, P) == True: # ensures that all necessary spaces are available
				qs.append(P) # will contain a pair coordinate for every ship
				B = [] # B will contain all points the ship is at
				x = P[0] # X - the X-coordinate of the ship
				y = P[1] # Y - the Y-coordinate of the ship
				if O in ("H", "h"): # if the ship is going horizontally, add the next x + size points to B
					for j in range(x, x + SZ):
						self.B[j][y] = "O"
						B.append([j, y])
				else: # if going vertically, add the next y + size points to B
					for j in range(y, y + SZ):
						self.B[x][j] = "O"
						B.append([x, j])
				self.Ships.append(B) # add all points in B to Ships
				Print(self.B) # display all the points the ship is at
			else:
				s = s-1 # if check is not successful, decrement and try again
			s = s + 1 # increment at the end of each loop
		return qs # return EX Hard Array
	pass
	
# Player:Place submenu: explain how to place ships
def Instructions():
	print("")
	print("TO PLACE YOUR SHIPS: ")
	print("Input whether the ship is Horizontal (H) or Vertical (V)")
	print("and the leftmost/uppermost coordinate in the format A-J, 1-10")
	print("Your input should look like this: H D9, V E10, etc")
	print("")
	pass
	
# checks if all required points on the board are available
def Check(board, orientation, size, point):
	x = point[0]
	y = point[1]
	for j in range(2): # ensure both x and y are between 0 and 9
		if point[j] > 9 or point[j] < 0:
			print("Point supplied is not valid!")
			return False
	# ensure that the ship does not go off the board due to length
	if orientation in ("H", "h"):
		if x + size > 9:
			print("Ship does not fit in that position!")
			return False
	elif orientation in ("V", "v"):
		if y + size > 9:
			print("Ship does not fit in that position!")
			return False
	else:
		print("Did not provide valid orientation")
	# ensure no other ships are already in those spots
	if orientation in ("H", "h"):
		for j in range(x, x + size):
			if board[j][y] == 'O':
				print("Another ship is already there!")
				return False
	else:
		for j in range(y, y + size):
			if board[x][j] == 'O':
				print("Another ship is already there!")
				return False
	# if all of these checks have passed, the ship is in a useable location
	return True

# the AI class
class AI:
	# A - where AI has attacked
	A = [[' ' for x in range(10)] for y in range(10)]
	# B - where AI's ships are placed
	B = [[' ' for x in range(10)] for y in range(10)]
	# Data - for storing read in from data.txt
	Data = [[0 for x in range(10)] for y in range(10)]
	# same as Player class
	Types = ["DESTROYER", "SUBMARINE","CRUISER","BATTLESHIP","CARRIER"]
	Sizes = [2, 3, 3, 4, 5]
	Ships = []
	# AI- exclusive arrays
	Starting = [] # where the uppermost corners of player ships are located - only used in EX Hard Mode
	P_Queue = [] # high priority attack queue
	Queue = [] # regular priority attack queue 
	MAD = False # whether the game is in Mutually Assured Destruction Mode or not
	mode = 1 # game mode the player has set
	option = 1 # options the player has set
	range = 1 # range of weapon attacks
	def Read(self): # reads data.txt
		f = open('data.txt')
		y = 0
		for line in f:
			for x in range(10):
				self.Data[x][y] = int(line[x])
			y = y + 1
		f.close()
	def Write(self): # rewrites data.txt at the end of play
		f = open('data.txt', 'w')
		for y in range(10):
			for x in range(10):
				c = str(self.Data[x][y])
				f.write(c)
			f.write("\n")
		f.close()
	def Place(self): # AI places its ships at random across the board
		s = 0 # loop counter
		d = ["V", "H"] # to randomly determine Horizontal or Vertical placement
		while s < 5: # places all five ships
			SZ = self.Sizes[s] # size
			import random # for random placement
			random.seed()
			O = d[random.randrange(2)] # determines orientation
			x = random.randrange(10) # X coordinate
			y = random.randrange(10) # Y coordinate
			P = [x, y] # make pair
			if Check_A(self.B, O, SZ, P) == True: # check coordinates for collision
				B = [] # same as Player but places automatically
				if O in "H":
					for j in range(x, x + SZ):
						self.B[j][y] = "O"
						B.append([j, y])
				else:
					for j in range(y, y + SZ):
						self.B[x][j] = "O"
						B.append([x, j])
				self.Ships.append(B)
			else:
				s = s-1
			s = s + 1
	def Queue_Setup(self):
		for j in self.Starting: # takes player starting points and updates Data accordingly
			x = j[0]
			y = j[1]
			self.Data[x][y] = self.Data[x][y] + 1
		decrement = True # whether to decrease all values in Data by 1
		for m in self.Data: # make sure all values in Data are less than 9 but greater than 0
			for n in m:
				if n > 9:
					n = 9
				if n == 0:
					decrement = False
		if decrement == True: # if all values are greater than 0, decrease them all by 1
			for m in self.Data:
				for n in m:
					n = n - 1
		w = 9 # loop counter
		while w > 0:
			m = 0 # inside loop counter
			while m < 10:
				n = 0 # inner inner loop counter
				while n < 10:
					if self.Data[m][n] == w: # if point[m][n] equals w, add it to the regular priority Attack Queue
						q = [m, n]
						self.Queue.append(q)
					n = n + 1
				m = m + 1
			w = w - 1
		self.Write() # after that's done, write Data back to file
		pass
	pass

def Check_A(board, orientation, size, point): # ensure that AI-determined points are good for placement
	# effectively same as Player version
	x = point[0]
	y = point[1]
	for j in range(2):
		if point[j] > 9 or point[j] < 0:
			return False
	if orientation in ("H"):
		if x + size > 9:
			return False
	elif orientation in ("V"):
		if y + size > 9:
			return False
	else:
		print("Did not provide valid orientation") # will not print for AI, can only be H or V
	if orientation in ("H"):
		for j in range(x, x + size):
			if board[j][y] == 'O':
				return False
	else:
		for j in range(y, y + size):
			if board[x][j] == 'O':
				return False
	# all checks passed, return
	return True

# ensure that a set of coordinates has X, Y values between 0 and 9
def Valid(point):
	x = point[0]
	y = point[1]
	if x > 9 or x < 0:
		return False
	if y > 9 or y < 0:
		return False
	return True

# when the AI wins, prints different things depending on game mode/option set
def Victory_A(mode, option):
	if mode == 1:
		print("It seems I have scraped together a victory")
	elif mode == 2:
		print("My programming has come through and seized victory")
	elif mode == 3:
		print("My defeat was never really on the table, anyway")
	if option == 2:
		print("But truly, the only way to win, is to not play") # another shoutout to the classic film War Games, even if this isn't tic-tac-toe
	elif option == 3:
		print("So much for the \'Mutual\' part of the destruction, I suppose")
	elif option == 4:
		print("It is in the most hopeless situations, that one's true colors appear")
	
# prints gameboard
def Print(f):
	print(" ", end=" ")
	for j in range(10):
		print(chr(j + 65), end="")
	print("\n  ----------")
	for y in range(10):
		r = y+1
		if r == 10:
			r = 0
		print(r, end="|")
		for x in range(10):
			print(f[x][y], end='')
		print("")
	pass
	
# converts 0-9 to traditional Battleship coordinates
# 0,0 to A1; 3,4 to D5, etc
def PointToPair(s):
	if len(s) == 1:
		return 10, 10
	# convert A-J to 1-10
	a = ord(s[0]) - 65
	# convert 1-10 to int
	b = int(s[1:]) - 1
	c = [a, b]
	return c
	pass
	
# converts coordinates back into 0-9 pair
def PairToPoint(s):
	a = chr(s[0] + 65)
	a = a + str(s[1] + 1)
	return a

# Here begins the actual program
# Print Header
print("")
print("                    B A T T L E B O T                     ")
print("                         3 0 0 0                          ")
print("")
print("THE MOST EXTRAORDINARY 'BATTLESHIP' SIMULATOR KNOWN TO MAN")
print("")
# create Player and AI objects
a = AI()
a.Read()
p = Player()

# start game or access help menu
select = "H"
while not (select == "S" or select == "s"):
	print("INPUT 'H' FOR HELP, OR 'S' TO START GAME")
	select = input("> ")
	if select in ("H", "h"):
		Help()

# Select AI Difficulty
select = "M"
while (select == "M"):
	print("PLEASE INPUT YOUR PREFERRED MODE OF PLAY")
	select = input("> ")
	if select in ("1"):
		a.mode = 1
		PvA1()
	elif select in ("2"):
		a.mode = 2
		PvA2()
	elif select in ("3"):
		a.mode = 3
		PvA3()
	else:
		print("Invalid entry, enter a number 1-3")
		select = "M"

# Select Game Option
select = "O"
while (select == "O"):
	print("SELECT OPTION")
	select = input("> ")
	if select in ("1"):
		print("DEFAULT MODE SELECTED")
		a.option = 1
	elif select in ("2"):
		MUTUALLY_ASSURED()
		a.option = 2
	elif select in ("3"):
		ALL_OUT()
		a.option = 3
		a.range = 3
		p.range = 3
	elif select in ("4"):
		ATF()
		a.option = 4
		a.range = 3
	else:
		print("Invalid entry, enter a number 1-4")
		select = "O"

# Play Begins
a.Place() # AI places their pieces
a.Starting = p.Place() # Player places their pieces
a.Queue_Setup() # AI sets up Attack Queue
turnCount = 1
gameOver = False
import random
while (gameOver == False):
	print("Player Turn ", end="") # print what turn it is
	print(turnCount)
	success = False
	s = 0 # attack coordinate pair
	x = 0 # x coordinate of pair
	y = 0 # y coordinate of pair
	while success == False:
		Print(p.A) # print where player has attacked so far
		print("Please input the enemy space you would like to attack")
		s = input("> ") # get input
		s = PointToPair(s)
		x = s[0]
		y = s[1]
		if x > 9 or y > 9 or x < 0 or y < 0: # check for valid input
			print("Please try again")
		elif p.A[x][y] not in ' ':
			print("You have already attacked that space")
		else: 
			success = True # previously not attacked space found
	# if AI ship map is blank at that space, a miss
	if a.B[x][y] == ' ':
		p.A[x][y] = 'X' # player attack map adds an X for miss
		print("You have missed")
	# otherwise, it's a hit!
	else:
		p.A[x][y] = 'H' # player attack map adds an H for Hit
		print("A hit! A hit!")
		for m in a.Ships:
			for n in m:
				if n == s:
					m.remove(n) # find the point on the ship that was hit and remove it from the array
			if len(m) == 0: # if all points have been removed from the array, the ship has been sunk
				print("- You have successfully sunk the enemy", end=" ")
				sunk = a.Types[a.Ships.index(m)] # print the name of the ship that was sunk
				print(sunk)
				a.Types.remove(sunk) # and remove it from the array accordingly
				a.Ships.remove(m)
		if len(a.Types) == 0: # if all types of ships have been removed, the game is over
			gameOver = True
			print("Congratulations, you have won!")
			break
	# Now begins the computer's turn
	input("Press Enter key to continue to computer turn")
	print("Computer is now making move")
	success = False
	while success == False: # AI finds point to attack
		if a.mode == 3 and turnCount % 4 == 0 and len(a.Starting) > 0: # if EX Hard Mode is enabled, cheat every four turns
			val = a.Starting[0]
			x = val[0]
			y = val[0]
			a.Starting.pop(0)
		elif a.mode == 2 or a.mode == 3: # if Hard Mode is enabled, use Attack Queue to determine next move
			if len(a.P_Queue) > 0: # attack from Priority Queue first
				val = a.P_Queue[0]
				x = val[0]
				y = val[1]
				a.P_Queue.pop(0)
				pass
			elif len(a.Queue) > 0:
				random.seed # otherwise take a random number from the regular attack queue and strike there
				pos = random.randrange(len(a.Queue))
				val = a.Queue[pos]
				x = val[0]
				y = val[1]
				a.Queue.remove(val)
			else: # if Regular and Priority Queues are empty, attack at random
				random.seed
				x = random.randrange(10)
				y = random.randrange(10)
		else: # if Easy Mode is enabled, attacks are always at random
			random.seed
			x = random.randrange(10)
			y = random.randrange(10)
		if a.A[x][y] == ' ': # ensures chosen point has not yet been attacked
			success = True
			s = [x, y]
	print("Attacking point ", end="") # print where is being attacked
	print(PairToPoint(s))
	if p.B[x][y] == ' ':
		a.A[x][y] = 'X'
		print("Miss") # if player's board reads a blank space at that location, it is a miss
	else:
		a.A[x][y] = 'H' # otherwise, it's a hit
		p.B[x][y] = 'H'
		print("Hit")
		# add points surrounding the hit to the Priority Queue
		pqW = [x-1, y]
		pqN = [x, y-1]
		pqS = [x, y+1]
		pqE = [x+1, y]
		pqF = [pqW, pqN, pqS, pqE]
		# check that points to be added are valid before inserting them
		for PT in pqF:
			if Valid(PT) == True:
				a.P_Queue.insert(0, PT)
		for m in p.Ships:
			for n in m:
				if n == s:
					m.remove(n) # remove point from Ship in Player's side
			if len(m) == 0: # if all points have been removed, ship has been sunk
				print("- Your", end=" ")
				sunk = p.Types[p.Ships.index(m)]
				print(sunk, end=" ")
				print("has been sunk")
				p.Types.remove(sunk)
				p.Ships.remove(m)
				a.P_Queue.clear()
	print("The state of your fleet:")
	Print(p.B) # prints player fleet
	input("Press Enter key to continue")
	if turnCount > 9 and a.option == 4: # end of game under Absolute Terror Field
		p.Types.clear()
		print("Time is up. Absolute Terror Field established.")
	if len(p.Types) == 0: # if all ships have been removed from Player's field, the game is over
		gameOver = True
		Victory_A(a.mode, a.option)
	turnCount = turnCount + 1
print("")
print("                    G A M E  O V E R                      ")
pass