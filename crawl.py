from denizen.player import Player
from dungeon.dungeon import Dungeon

# Welcome the player
print('Welcome to Dungeon Crawler')

# Initialize the environment
dungeon = Dungeon()
current_room = dungeon.get_starting_point()

# Initialize the player
health = 10
player = Player(health)

# Start the game
playing = True

print('You\'re standing in ' + current_room.look())

while playing:
    action = input("--> ")

    if action == 'look':
        print("You're standing in " + current_room.look())
    elif current_room.has_action_to_reach_room(action):
        current_room = current_room.move(action)
        print("You're standing in " + current_room.look())
    elif action == 'exit':
        print("Exiting Dungeon Crawler")
        playing = False
        print()
    else:
        print("The action '" + action + "' wasn't recognized.")


# Bid the player farewell
print('Thanks for playing!')
print('- Twinnrova')
print()
exit()