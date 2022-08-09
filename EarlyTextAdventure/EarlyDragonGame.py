# Early concept of Text adventure game. Explored understandings of how to traverse rooms.
# By Richard Elphinstone.
# List of functions
def show_intro():
   # Print a main menu and the commands.
   print('**********')
   print("Simplified Dragon Text Adventure Game")
   print("No need to collect anything. Explore! As the Dragon is not here.")
   print('**********')
   print("Move commands: go South, go North, go East, go West")
   print('Type exit to quit the game or Help for instruction.')

def instructions():
    # Print a list of commands.
    print('Move Commands: go South, go North, go East, go West')
    print('Type exit to quit the game.')

def moving_rooms(direction, room = 'Great Hall'):
    # Function for moving player from room to room.
    if direction in rooms[room]:  # Check if direction is available.
        print('You just moved rooms')
        if direction == 'North':
            return rooms[room]['North']
        if direction == 'South':
            return rooms[room]['South']
        if direction == 'East':
            return rooms[room]['East']
        if direction == 'West':
            return rooms[room]['West']
    else:
        print('You can not go that way!')  # Invalid direction for room.
        return current_room

def player_status():
    # Current player location.
    print('----------\nYou are currently in the {}\n'
          '----------'.format(current_room))

# Dictionary of Rooms and options listed in game.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

# Game set-up
current_room = 'Great Hall'
show_intro()

# Loop for input of player commands.
while current_room != 'Exit':
    player_status()
    user_input = input('Type Command\nOr type exit to quit game.\n')
    if user_input == 'exit':
        current_room = 'Exit'
    elif user_input == 'go North':
        current_room = moving_rooms('North', current_room)
    elif user_input == 'go South':
        current_room = moving_rooms('South', current_room)
    elif user_input == 'go East':
        current_room = moving_rooms('East', current_room)
    elif user_input == 'go West':
        current_room = moving_rooms('West', current_room)
    elif user_input == 'Help':
        instructions()
    else:
        print('That does not make sense. Please Try a Command.'
              '\nType Help for Instructions')  # Invalid command.
print('Thank you for playing! Good Bye!')  # Player has quit game.
