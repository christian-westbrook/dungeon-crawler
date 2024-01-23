class Room:
    def __init__(self, description):
        self.description = description
        self.connections = {}
    
    def look(self):
        return self.description
    
    def move(self, action_to_reach_room):
        if action_to_reach_room in self.connections:
            return self.connections[action_to_reach_room]
        else:
            return self
    
    def add_connection(self, action_to_reach_room, room):
        self.connections[action_to_reach_room] = room