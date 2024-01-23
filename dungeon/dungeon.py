from dungeon.room import Room

class Dungeon:
    def __init__(self):
        
        # Rooms
        leaky_room = Room('a leaky room')
        hallway = Room('a dusty hallway with a pair of wooden doors at one end and an opening on the other')

        self.starting_point = leaky_room
    
    def get_starting_point(self):
        return self.starting_point

