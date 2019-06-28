#improvement notes
#consider using a module for replacing what I have as global variables
#e.g. import config that include game_time = 0 that can be called on as config.gametime


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
]


#inventory information in a dictionary
player_inventory = []


class Player:
    def __init__(self,player_name):
        self.player_name = player_name
        self.has_ticket = False
        self.has_sword = False
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

#player can pick up a few different items    
    def buy_ticket(self):
        self.has_ticket = True
        player_inventory.append('Ticket')
        print('Great! You now have a ticket. You can verify that if you type "bag"')
        time.sleep(1)
    
    def pickup_sword(self):
        self.has_sword = True
        player_inventory.append('Sword')
        print('You picked up and sword and feel powerful.')
        time.sleep(1)


#since time progressing, we need a function for "waiting"    
    def waiting(self):
        print('--- You decide to wait. If you wanted to move, try typing one of the direction options. ---')
        time.sleep(1)

    def game_over(self):
        print("G A M E  O V E R!")
        exit()


class Location:
    def check_train_present(self):
        global train_present
        if game_time % 4 == 0:
            train_present = True
            print('Chooo! Choooo! The train has just arrived.')
            print('--Option-- west: Enter the train')
        else:
            train_present = False

import time
game_time = 0
train_present = False
location_number = 0

#establishing a "time limit" to the game   
def time_limit():
    if game_time == 20:
        print("Unfortunately, you didn't make it to work on time")
        Player.game_over(player_name)

def start_platform():
    global player_name
    global game_time
    global train_present
    global location_number
    #every time you change location, the current_location is set to the appropriate number
    location_number = 0
    game_time += 1
    time_limit()
    print('Turn',game_time)
    print(locations[0]['description'])
    Location.check_train_present(start_platform)
    print(locations[0]['options'])
    choice = input('What do you want to do?  ')

#testing how to make the choice section dryer
    # if choice in choices[0]:
    #     print(choices[0][choice])
    # else:
    #     print('test')

#choice section
    if choice == 'north':
        ticket_booth()
    elif choice == 'south':
        bench()
    elif choice == 'west' and train_present:
        train_car3()
    elif choice == 'bag':
        Player.check_inventory(player_inventory)
        start_platform()
    else:
        player_name.waiting()
        start_platform()


# have a function that checks if train is there and if present, allow you to do it
def train_check_and_move():
    global train_present
    if train_present == True:
        train_car3()
    else:
        current_location()

def check_bag():
	Player.check_inventory(player_inventory)
	current_location()
def buy_ticket():
	Player.buy_ticket(player_name)
	ticket_booth()
def pickup_sword():
	Player.pickup_sword(player_name)
	train_car1()

def ticket_booth():
    global game_time
    global train_present
    global location_number
    print(location_number)
    location_number = 1
    print(location_number)
    game_time += 1
    time_limit()
    print('Turn',game_time)
    print(locations[1]['description'])
    Location.check_train_present(ticket_booth)
    #print the options
    print(locations[1]['options'])
    choice = input('What do you want to do?  ')
    if choice == 'buy':
        if "Ticket" in player_inventory:
            print('You already have a ticket.')
            time.sleep(1)
            game_time -= 1
            ticket_booth()
        else: 
            Player.buy_ticket(player_name)
            ticket_booth()
    elif choice == 'south':
        start_platform()
    elif choice == 'west' and train_present:
        train_car3()
    elif choice == 'bag':
        Player.check_inventory(player_inventory)
        time.sleep(1)
        #checking your bag shouldn't progress game_time
        game_time -= 1
        ticket_booth()
    else:
        Player.waiting(player_name)
        ticket_booth()

def bench():
    global game_time
    global train_present
    game_time += 1
    time_limit()
    print('Turn',game_time)
    print(locations[2]['description'])
    Location.check_train_present(bench)
    print(locations[2]['options'])
    choice = input('What do you want to do?  ')
    if choice == 'sit':
        Player.waiting(player_name)
        bench()
    elif choice == 'north':
        start_platform()
    elif choice == 'west' and train_present:
        train_car3()
    elif choice == 'bag':
        Player.check_inventory(player_inventory)
        time.sleep(1)
        #checking your bag shouldn't progress game_time
        game_time -= 1
        ticket_booth()
    else:
        Player.waiting(player_name)
        ticket_booth()

def train_car5():
    global game_time
    global train_present
    game_time += 1
    time_limit()
    print('Turn',game_time)
    print(locations[7]['description'])
    print(locations[7]['options'])
    choice = input('What do you want to do?  ')
    if choice == 'fight':
        if "Sword" in player_inventory:
            print('You slice the monster in half and become a hero.')
            print('What a great story to tell coworkers.')
            print('Y O U  W I N ! ! !')
        else: 
            print('You try to punch the monster...')
            print('The monster is unaffected and claws you to death.')
            game_over()
    elif choice == 'north':
        train_car4()
    elif choice == 'west' and train_present:
        win_platform()
    elif choice == 'bag':
        Player.check_inventory(player_inventory)
        time.sleep(1)
        #checking your bag shouldn't progress game_time
        game_time -= 1
        train_car5()
    else:
        Player.waiting(player_name)
        train_car5()

def train_car1():
    global game_time
    global train_present
    game_time += 1
    time_limit()
    print('Turn',game_time)
    print(locations[3]['description'])
    print(locations[3]['options'])
    choice = input('What do you want to do?  ')
    if choice == 'sword':
        if "Sword" in player_inventory:
            print('You already have the sword')
            time.sleep(1)
            game_time -= 1
            train_car1()
        else: 
            player_name.pickup_sword()
            train_car1()
    elif choice == 'south':
        train_car2()
    elif choice == 'west' and train_present:
        win_platform()
    elif choice == 'bag':
        Player.check_inventory(player_inventory)
        time.sleep(1)
        #checking your bag shouldn't progress game_time
        game_time -= 1
        train_car1()
    else:
        Player.waiting(player_name)
        train_car1()

#moved outside of Player class. consider using a "factory function" via staticmethod in Player class in the future
def intro():
    print('--- Intro ---')
    print('Welcome to your daily commute.')
    print('To win the game, become a hero and get to work safely.')
    time.sleep(1)
    return input('What is your name?')



#testing using a function as a dict value and invoking it via input
def test():
    print('testing')

choices = [
{
#Location 0 
'name' : start_platform,
'north' : ticket_booth,
'south' : bench,
'west' : train_check_and_move
},
{
#Location 1
'name' : ticket_booth,
'buy' : buy_ticket,
'south' : start_platform,
'west' : train_check_and_move
},
{
#Location 2
'name' : bench,
'north' : start_platform,
'west' : train_check_and_move
},
{
#Location 3
'name' : train_car1,
'sword' : pickup_sword,

},
]

print(location_number)



location_number = 3
current_location = choices[location_number]['name']
current_location()


# choice = input('type north')
# if choice in choices[0]:
#     choice_function = choices[0][choice]
#     choice_function()
# else:
#     print('test')




#returns the name of the player
# player_name = intro()
# #creates the player_name object using Player class
# player_name = Player(player_name)




# def main():
#     intro()
#     start_platform()

# if __name__ == "__main__":
#     main()







