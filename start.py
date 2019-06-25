

### NOTES ### 
#room information in a dictionary
rooms = {}


#inventory information in a dictionary
player_inventory = {}


#inventory items can be picked up

#consider functions that kept on asking for an answer until the user supplies a valid answer

#define global variables like if the player has certain items which would initiatlt be set to false
#OR
#use class to define a player that has properties
class Player:
    def __init__(self):
        self.player_name = player_name
        self.has_ticket = False

    #consider a player can move?
    #def move_west(self):

#player_name = input('What is your name?')
#print(player_name)


#has_ticket = False

game_time = 0
train_present = False

def start_platform():
	global game_time
	global train_present
	game_time += 1
	print('Turn',game_time)
	check_train_present()
	print('You are at a train station platform.')
	print('north: Ticket booth')
	print('south: Go sit on a bench')
	print('wait: Wait awhile')

	if train_present:
		print('The train has just arrived.')
		print('west: Enter the train')

	choice = input('? ')
	if choice == 'north':
		ticket_booth()
	elif choice == 'south':
		bench()
	elif choice == 'west' and train_present:
		train_car3()
	else:
		start_platform()

def check_train_present():
	global train_present
	if game_time % 4 == 0:
		train_present = True
	else:
		train_present = False


start_platform()
	
