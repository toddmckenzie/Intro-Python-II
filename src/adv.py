from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'
# Make a new player object that is currently in the 'outside' room.

player = Player("outside")

# player = Player("treasure")
# Write a loop that:
#
# print(player.currentRoom)
flag = True
while flag == True:
    for i in room:
        if i == player.currentRoom:
            print(room[i].name)
            print(room[i].description)
            move = input("Would you like to move n, s, e, w?")
            if move == 'q' or move == 'quit':
                flag = False
            elif move == 'n':
                player.changeRoom(room[i].n_to)
            elif move == 's':
                player.changeRoom(room[i].s_to)
            elif move == 'e':
                player.changeRoom(room[i].e_to)
            elif move == 'w':
                player.changeRoom(room[i].w_to)
# * Prints the current room name // 
# * Prints the current description (the textwrap module might be useful here). // 
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


# to change room call player.changeRoom(newRoom)