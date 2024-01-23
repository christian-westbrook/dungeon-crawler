class Creature:
    def __init__(self, health):
        self.maximum_health = health
        self.current_health = self.maximum_health
    
    def getHealth(self):
        return self.current_health
