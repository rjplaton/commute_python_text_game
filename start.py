

### NOTES ### 
#room information in a dictionary
rooms = {}


#inventory information in a dictionary
player_inventory = ['--- Sword','--- Pen']


#inventory items can be picked up

#consider functions that kept on asking for an answer until the user supplies a valid answer

#define global variables like if the player has certain items which would initiatlt be set to false
#OR
#use class to define a player that has properties
class Player:
    def __init__(self):
        self.player_name = player_name
        self.has_ticket = False
        self.has_sword = False
        self.has_pen = False
        self.has_zombiearm = False

    def check_inventory(self):
    	for items in player_inventory:
    		print(items)


    #consider a player can move?
    #def move_west(self):

#Pseudocode if we want to create a location class
class Location:
    def __init__(self):
        self.train_present = False
        self.description = description
        self.choices = choices



#player_name = input('What is your name?')
#print(player_name)


#has_ticket = False
import time
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
	elif choice == 'bag':
		Player.check_inventory(player_inventory)
		time.sleep(1)
		#checking your bag shouldn't progress game_time
		game_time -= 1
		start_platform()
	else:
		print('--- You decide to wait. If you wanted to move, try typing one of the direction options. ---')
		time.sleep(1)
		start_platform()

def check_train_present():
	global train_present
	if game_time % 4 == 0:
		train_present = True
	else:
		train_present = False


start_platform()
	
