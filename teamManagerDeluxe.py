class Player(object):

        def __init__(self, player_name, player_age, goals, jersey_num, position):

                self.player_name = player_name
                self.player_age = player_age
                self.goals = goals
		self.jersey_num = jersey_num
		self.position = position 

        def showPlayer(self):
                print("Name: " + str(self.player_name))
                print("Age: " + str(self.player_age))
		print("Goals: " + str(self.goals))
		print("Jersey Number: " + str(self.jersey_num))
		print("Position: " + str(self.position))

# put players into a list
my_players = []

print("Welcome to Team Manager Deluxe!")
print("Do you want to start with a new team or open an existing team?")
print("Enter the number of your choice and press enter.")
print("(1) Start with a new team")
print("(2) Open a file for an existing team")

# takes the playerList and the user's desired filename
# writes each Player to file
def saveTeam(playerList, filename):
	file = open(filename, 'w')
 
	# write to the file
	for p in playerList:
		file.write(p.player_name + " " + str(p.player_age) + " " + str(p.goals) + " " + str(p.jersey_num) + " " + p.position + "\n")   
	# close the file
 	file.close()

 
# takes a filename for a file of players
# returns a list of Players
def loadTeam(filename):
 
    # create empty list
	team = []
    # open the file
	file = open(filename, 'r')
    # read each line and create Player from it (use a loop)
	line = file.readline()
	while line != " ": 
		my_player = my_line.split()
		team.append(Player(name, age, goals, jersey_num, position))
		print(my_player[0]) 	
        # split each line into a list of the variables
		line = file.readline()
        # read each next line
 
    # close the file
		file.close()		
    # return the completed list
 
    # placeholder - delete once the function is complete
	pass


choice = int(raw_input())

while choice != 0: 
	if choice == 1:
		print("What is your players name?")
		name = str(raw_input())
		print("How old is your player?")
		age = int(raw_input()) 
		print("How many goals has your player made?")
		goals = int(raw_input())
		print("What is your players jersey number?")

		jersey_num = int(raw_input())
		print("What is your players position?")
		position = str(raw_input())
		my_players.append(Player(name, age, goals, jersey_num, position))
		
		print("choose an option")
                print("option 1 is to add players to the team")
                print("option 2 is to view the players")
                print("option 3 is to save the team to a file")

		choice = int(raw_input())

	elif choice == 2:
		for p in my_players:
			p.showPlayer()
		print("choose an option")
		print("option 1 is to add players to the team")
		print("option 2 is to view the players")
		print("option 3 is to save the team to a file")
		choice = int(raw_input())

	elif choice == 3:
		print("what do you want to call the file?")
		filename = raw_input()	
		saveTeam(my_players, filename)

		print("choose an option")
                print("option 1 is to add players to the team")
                print("option 2 is to view the players")
                print("option 3 is to save the team to a file")
                choice = int(raw_input())
	

my_players.append(Player(name, age, goals))

# call our showPlayer funtion for all of our Player objects 
for p in my_players:
        p.showPlayer()


