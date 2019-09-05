# Write a class to hold player information, e.g. what room they are in
# currently.

class Player(): 
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
    
    def changeRoom(self, newRoom):
        self.currentRoom = newRoom

    def __str__(self):
        return ("Current room is: " + self.currentRoom)
        