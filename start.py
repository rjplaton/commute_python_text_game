

### NOTES ### 
#room information in a dictionary
locations = [
{
'name' : 'Starting Platform',
'description' : 'You are at the main train station platform.',
'options' : 
"""--Option-- north: Ticket booth
--Option-- south: Go sit on a bench
--Option-- wait: Wait awhile
"""
},
{
'name' : 'Ticket Booth',
'description' : "You walk up to the ticket booth. Lucky you, there isn't a line.",
'options' : 
"""--Option-- buy: Buy a ticket
--Option-- south: Starting area towards the bench
--Option-- wait: Wait awhile
"""
},
]

#print(locations['starting_platform'])

#inventory information in a dictionary
player_inventory = ['Sword','Pen']


#inventory items can be picked up

#consider functions that kept on asking for an answer until the user supplies a valid answer

#define global variables like if the player has certain items which would initiatlt be set to false
#OR
#use class to define a player that has properties
class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.has_ticket = False
        self.has_sword = False
        self.has_pen = False
        self.has_zombiearm = False

    def intro(self):
        print('--- Intro ---')
        print('Welcome to your daily commute.')
        print('To win the game, get to work safely.')
        player_name = input('What is your name?')
        player1 = Player(player_name)
        print('Hi', player1.player_name)

    def check_inventory(self):
    	print('--- | Bag Inventory |---')
    	i = 1
    	for items in player_inventory:
    		print('---',i,items)
    		i += 1
    
    def buy_ticket(self):
    	self.has_ticket = True
    	player_inventory.append('Ticket')
    
    def pickup_pen(self):
    	self.has_pen = True
    	player_inventory.append('Pen')

    def pickup_sword(self):
    	self.has_sword = True
    	player_inventory.append('Sword')
    
    def pickup_sword(self):
    	self.has_sword = True
    	player_inventory.append('Zombie Arm')
    
    def waiting(self):
        print('--- You decide to wait. If you wanted to move, try typing one of the direction options. ---')
        time.sleep(1)
        if game_time > 3:
            print("Unfortunately, you didn't make it to work on time")
            Player.game_over(self)
    def game_over(self):
        print("G A M E  O V E R!")
        exit()


#testing if these things work
player1 = Player('me')
player1.intro()
print(player1.has_ticket)
print(player_inventory)
player1.buy_ticket()
print(player1.has_ticket)
print(player_inventory)


#Pseudocode if we want to create a location class
class Location:
    def check_train_present(self):
        global train_present
        if game_time % 4 == 0:
            train_present = True
            print('Chooo! Choooo! The train has just arrived.')
            print('--Option-- west: Enter the train')
        else:
            train_present = False


    #def train_is_present(self):
        #global train_present
        #if train_present:
         #   print('Chooo! Choooo! The train has just arrived.')
          #  print('--Option-- west: Enter the train')
    #def description(self):
    	#print(locations[self])

#Location.description('starting_platform')

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
	print(locations[0]['description'])
	Location.check_train_present(start_platform)
	print(locations[0]['options'])
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
		Player.waiting(player1)
		start_platform()




start_platform()
	
