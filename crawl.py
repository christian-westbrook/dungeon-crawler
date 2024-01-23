from denizen.player import Player
from dungeon.dungeon import Dungeon

dungeon = Dungeon()
player = Player(10)

starting_point = dungeon.get_starting_point()

print('You\'re standing in ' + starting_point.look())