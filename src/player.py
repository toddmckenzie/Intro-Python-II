# Write a class to hold player information, e.g. what room they are in
# currently.

class Player(): 
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.items = []

    def changeRoom(self, newRoom):
        self.currentRoom = newRoom

    def addItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        self.items.remove(item)

    def __str__(self):
        return ("Current room is: " + self.currentRoom)
        