

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


def start_platform():
    print('You are at a train station platform.')
    print('The train has just arrived.')
    print('north: Ticket booth')
    print('west: Enter the train')
    print('south: Go sit on a bench')
    choice = input('? ')
    if choice == 'north':
        ticket_booth()
    elif choice == 'south':
        bench()
    elif choice == 'west':
        train_car3()
    else:
        start_platform()

start_platform()
	


if __name__ == "__main__":
    main()