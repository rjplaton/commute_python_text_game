#improvement notes
#consider using a module for replacing what I have as global variables
#e.g. import config that include game_time = 0 that can be called on as config.gametime
import time
game_time = 0
train_present = False
location_number = 0

#location information
locations = [
{
'name' : 'Starting Platform',
'description' : 'You are at the main train station platform.',
'options' : 
"""--Option-- north: Ticket booth
--Option-- south: Go sit on a bench
--Option-- wait: Wait awhile
--Option-- bag: Check your bag inventory
""",
},
{
'name' : 'Ticket Booth',
'description' : "You walk up to the ticket booth. Lucky you, there isn't a line.",
'options' : 
"""--Option-- buy: Buy a ticket
--Option-- south: Starting area towards the bench
--Option-- wait: Wait awhile
--Option-- bag: Check your bag inventory
""",
},
{
'name' : 'Bench',
'description' : "Nice. There's an open bench you can sit on.",
'options' : 
"""--Option-- sit: Walk to the bench and sit on it
--Option-- north: Head back to the starting area
--Option-- wait: Wait awhile standing
--Option-- bag: Check your bag inventory
""",
},
{
'name' : 'Train Car 1',
'description' : """You enter train car 1 and you see a sword.
It beckons you to pick it up.
You are the chosen one""",
'options' : 
"""--Option-- sword: Fulfill your destiny and pick up the sword!
--Option-- south: Move back to next train down
--Option-- wait: Wait awhile standing
--Option-- bag: Check your bag inventory
""",
},
{
'name' : 'Train Car 2',
'description' : "You enter train car 2 and it stinks.",
'options' : 
"""--Option-- north: Move to the next train up
--Option-- south: Head back to next train down
--Option-- wait: Wait awhile standing
--Option-- bag: Check your bag inventory
""",
},
{
'name' : 'Train Car 3',
'description' : "You try to enter train car 3 and squeeze in. It's full so try to move to another car because this is uncomfortable!",
'options' : 
"""--Option-- north: Move to the next train up
--Option-- south: Head back to next train down
--Option-- wait: Wait awhile standing and being annoyed
--Option-- bag: Check your bag inventory
""",
},
{
'name' : 'Train Car 4',
'description' : "You enter train car 4 and hear screaming from the next car southward. You are very curious!",
'options' : 
"""--Option-- north: Move to the next train up
--Option-- south: Investigate the car southward
--Option-- wait: Wait awhile standing and ignoring the screams
--Option-- bag: Check your bag inventory
""",
},
{
'name' : 'Train Car 5',
'description' : """You enter train car 5 and immediately see carnage.
In the middle of the car, the thing is staring at you""",
'options' : 
"""--Option-- fight: Fight the monster
--Option-- north: RUN back to next train up
--Option-- wait: Wait awhile standing
--Option-- bag: Check your bag inventory
""",
},
{
'name' : 'Lose Platform',
'description' : """You safely get off the train.
You have a sense of emptiness.""",
'options' : 
"""--Option-- work: Get to work
--Option-- wait: Wait awhile standing
--Option-- bag: Check your bag inventory
""",
},
{
'name' : 'Win Platform',
'description' : """You safely get off the train as a hero.
You realize you don't need to go to work""",
'options' : 
"""--Option-- work: Go to work anyway
--Option-- enjoy: Choose to enjoy life today by not going to work
--Option-- wait: Wait awhile standing
--Option-- bag: Check your bag inventory
""",
},
]


#inventory information in a dictionary
player_inventory = []


class Player:
    def __init__(self,player_name):
        self.player_name = player_name
        self.has_seen_monster = False


    #considered @staticmethod
    # def intro():
    #     # Player.intro
    #     print('....')
    #     return newly_created_player

    def check_inventory(self):
        global game_time
        print('--- | Bag Inventory |---')
        i = 1
        for items in player_inventory:
            print('---',i,items)
            i += 1
        time.sleep(1)
        #checking your bag shouldn't progress game_time
        game_time -= 1 




#establishing a "time limit" to the game   
def time_limit():
    if game_time == 20:
        print("Unfortunately, you didn't make it to work on time")
        Player.game_over(player_name)


def check_train_present():
    global train_present
    if game_time % 4 == 0:
        train_present = True
        print('Chooo! Choooo! The train has just arrived.')
        print('--New Option-- west: Enter the train')
    else:
        train_present = False

# have a function that checks if train is there and if present, allow you to do it
def train_check_and_move():
    global train_present
    if train_present == True:
        train_car3()
    else:
        current_location = choices[location_number]['name']
        current_location()



def check_bag():
    global location_number
    Player.check_inventory(player_inventory)
    print(location_number)
    print(location_number)
    current_location = choices[location_number]['name']
    current_location()

def buy_ticket():
    if 'Ticket' in player_inventory:
        print('You already have a ticket!')
        time.sleep(1)
        ticket_booth()
    else:
        player_inventory.append('Ticket')
        Player.has_ticket = True
        print('Great! You now have a ticket. You can verify that if you type "bag"')
        time.sleep(1)
        ticket_booth()

def pickup_sword():
    if 'Sword' in player_inventory:
    	print('You already have the sword and it is awesome.')
	train_car1()
    else:
	    player_inventory.append('Sword')
	    print('You picked up the sword and feel powerful.')
	    time.sleep(1)
	    train_car1()

#since time progressing, we need a function for "waiting"    
def waiting():
    global location_number
    print('--- You decide to wait. If you wanted to move, try typing one of the direction options. ---')
    time.sleep(1)
    current_location = choices[location_number]['name']
    current_location()

def game_over():
    print("G A M E  O V E R!")
    exit()

def fight():
    if "Sword" in player_inventory:
        print('You slice the monster in half and become a hero.')
        time.sleep(1)
        print('What a great story to tell coworkers.')
        time.sleep(1)
        print('The train arrives at the station and reality sets in.')
        win_platform()
    else: 
        print('You try to punch the monster...')
        print('The monster is unaffected and claws you to death.')
        game_over()

def win():
    print('You are awesome.')
    print("""
          _   _   _     _   _   _  
 / \ / \ / \   / \ / \ / \ 
( Y | o | u ) ( W | I | N )
 \_/ \_/ \_/   \_/ \_/ \_/ 
""")

#LOCATION FUNCTIONS

def location_choice():
    global player_name
    global game_time
    global train_present
    global location_number
    global current_location
    choice = input('''What do you want to do?        ''')
    if choice in choices[location_number]:
        choice_function = choices[location_number][choice]
        choice_function()
    else:
        print('''------------- Choose one of the options below:        ''')
        time.sleep(1)
        game_time -= 1
        current_location = choices[location_number]['name']
        current_location()

def location_starter():
    global player_name
    global game_time
    global train_present
    global location_number
    global current_location
    #game time progressing when you enter a new area
    game_time += 1
    time_limit()
    print('Turn',game_time)
    print(locations[location_number]['description'])
    print(locations[location_number]['options'])
    #check if the train is there and allow player to move west
    if location_number <= 2:
        check_train_present()
        location_choice()
    else:
        location_choice()

def start_platform():
    global player_name
    global game_time
    global train_present
    global location_number
    global current_location
    #every time you change location, the current_location is set to the appropriate number
    location_number = 0
    location_starter()
    
def ticket_booth():
    global player_name
    global game_time
    global train_present
    global location_number
    global current_location
    location_number = 1
    location_starter()

def bench():
    global player_name
    global game_time
    global train_present
    global location_number
    global current_location
    location_number = 2
    location_starter()

def train_car1():
    global player_name
    global game_time
    global train_present
    global location_number
    global current_location
    location_number = 3
    location_starter()

def train_car2():
    global player_name
    global game_time
    global train_present
    global location_number
    global current_location
    location_number = 4
    location_starter()

def train_car3():
    global player_name
    global game_time
    global train_present
    global location_number
    global current_location
    location_number = 5
    location_starter()

def train_car4():
    global player_name
    global game_time
    global train_present
    global location_number
    global current_location
    location_number = 6
    location_starter()

def train_car5():
    global player_name
    global game_time
    global train_present
    global location_number
    global current_location
    location_number = 7
    location_starter()

def lose_platform():
    global player_name
    global game_time
    global train_present
    global location_number
    global current_location
    location_number = 8
    location_starter()

def win_platform():
    global player_name
    global game_time
    global train_present
    global location_number
    global current_location
    location_number = 9
    location_starter()


#LOCATION FUNCTIONS END


def intro():
    print('--- Intro ---')
    print('Welcome to your daily commute.')
    print('To win the game, become a hero, feel fulfilled and maybe get to work safely.')
    time.sleep(1)
    return input('What is your name?')

def debug():
    global player_name
    global game_time
    global train_present
    global location_number
    global current_location
    print(current_location)
    current_location = choices[location_number]['name']
    current_location()


#List of choices in a dict

choices = [
{
#Location 0 
'name' : start_platform,
'north' : ticket_booth,
'south' : bench,
'west' : train_check_and_move,
'wait' : waiting,
'bag' : check_bag,
'where' : debug,
},
{
#Location 1
'name' : ticket_booth,
'buy' : buy_ticket,
'south' : start_platform,
'west' : train_check_and_move,
'wait' : waiting,
'bag' : check_bag,
'where' : debug,
},
{
#Location 2
'name' : bench,
'north' : start_platform,
'west' : train_check_and_move,
'sit' : waiting,
'bag' : check_bag,
'where' : debug,
},
{
#Location 3
'name' : train_car1,
'sword' : pickup_sword,
'south' : train_car2,
'wait' : waiting,
'bag' : check_bag,
'where' : debug,
},
{
#Location 4
'name' : train_car2,
'north' : train_car1,
'south' : train_car3,
'wait' : waiting,
'bag' : check_bag,
'where' : debug,
},
{
#Location 5
'name' : train_car3,
'north' : train_car2,
'south' : train_car4,
'wait' : waiting,
'bag' : check_bag,
'where' : debug,
},
{
#Location 6
'name' : train_car4,
'north' : train_car3,
'south' : train_car5,
'wait' : waiting,
'bag' : check_bag,
},
{
#Location 7
'name' : train_car5,
'fight' : fight,
'north' : train_car4,
'wait' : waiting,
'bag' : check_bag,
'where' : debug,
},
{
#Location 8
'name' : lose_platform,
'work' : game_over,
'wait' : waiting,
'bag' : check_bag,
'where' : debug,
},
{
#Location 9
'name' : win_platform,
'work' : game_over,
'enjoy' : win,
'wait' : waiting,
'bag' : check_bag,
'where' : debug,
},
]


def main():
    #returns the name of the player
    player_name = intro()
    #creates the player_name object using Player class
    player_name = Player(player_name)
    start_platform()

if __name__ == "__main__":
    main()
