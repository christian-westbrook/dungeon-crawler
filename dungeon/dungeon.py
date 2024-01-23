from dungeon.room import Room

class Dungeon:
    def __init__(self):
        
        # Rooms
        leaky_room = Room('a leaky room. There\'s a bed and a wooden door.')
        self.starting_point = leaky_room

        hallway = Room('a dusty hallway with a wooden door at one end and an opening at the other.')
        leaky_room.add_connection('door', hallway)
        hallway.add_connection('door', leaky_room)

        inn = Room('a drafty inn. You\'re surrounded by empty chairs. It\'s dark and the wind is howling. There\'s an opening to a hall and a wooden door that looks like an entrance.')
        hallway.add_connection('opening', inn)
        inn.add_connection('hallway', hallway)
    
    def get_starting_point(self):
        return self.starting_point

