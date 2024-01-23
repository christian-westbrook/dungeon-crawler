from denizen.player import Player
from dungeon.dungeon import Dungeon

print('Welcome to Dungeon Crawler')

# Initialize environment
dungeon = Dungeon()
current_room = dungeon.get_starting_point()

# Initialize player
player = Player(10)

playing = True

print('You\'re standing in ' + current_room.look())

while playing:
    command = input('--> ')

    if command == 'look':
        print('You\'re standing in ' + current_room.look())
    if command == 'exit':
        print('Exiting Dungeon Crawler')
        print('Thanks for playing!')
        exit()