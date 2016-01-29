class Player(object):

        def __init__(self, player_name, player_age, goals):

                self.player_name = player_name
                self.player_age = player_age
                self.goals = goals

        def showPlayer(self):
                print("Name: " + str(self.player_name))
                print("Age: " + str(self.player_age))
		print("Goals: " + str(self.goals))

# put players into a list
my_players = []

print("choose an option")
print("option 1 is to add players to the team")
print("option 2 is to view the players")

options = int(raw_input())

while options != 0: 
	if options == 1:
		print("What is your players name?")
		name = str(raw_input())
		print("How old is your player?")
		age = int(raw_input()) 
		print("How many goals has your player made?")
		goals = int(raw_input())
		my_players.append(Player(name, age, goals))
		print("choose an option")
		print("option 1 is to add players to the team")
		print("option 2 is to view the players")
		options = int(raw_input())

	elif options == 2:
		for p in my_players:
			p.showPlayer()
		print("choose an option")
		print("option 1 is to add players to the team")
		print("option 2 is to view the players")
		option = int(raw_input())

my_players.append(Player(name, age, goals))

# call our showPlayer funtion for all of our Player objects 
for p in my_players:
        p.showPlayer()


