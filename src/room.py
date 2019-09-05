# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
    
    def __str__(self):
        return ("name: " + self.name + " Description: " + self.description)

    def addItem(self, item):
        self.items.append(item)
        
    def dropItem(self, item):
        self.items.remove(item)