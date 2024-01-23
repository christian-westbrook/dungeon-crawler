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
    command = input('--> ')

    if command == 'look':
        print('You\'re standing in ' + current_room.look())
    if command == 'exit':
        print('Exiting Dungeon Crawler')
        playing = False
        print()
    else:
        current_room = current_room.move(command)
        print('You\'re standing in ' + current_room.look())


# Bid the player farewell
print('Thanks for playing!')
print('- Twinnrova')
print()
exit()