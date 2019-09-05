from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     ["hammer", "old map"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["lamp", "walking stick"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["book", "sword"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["flashlight", "bell"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["Note: Sorry I took the gold", "donut"]),
}


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

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
            print("\n")
            print(room[i].name)
            print("\n")
            print(room[i].description)
            print("\n")
            if len(player.items) > 1:
                print("You have a " + player.items[0] + " and a " + player.items[1])
            if len(player.items) == 1:
                print("You have a " + player.items[0])
            if len(room[i].items) == 2:
                print("On the ground is a " + room[i].items[0] + " and a " + room[i].items[1])
            if len(room[i].items) == 1:
                 print("On the ground is a " + room[i].items[0])
            print("\n")  
            if len(room[i].items) == 2:
                pickup = input("\nWould you like to pick up " + room[i].items[0] + " or the " + room[i].items[1] + "? If so type in the name of the item you wish to pickup.")
            if len(room[i].items) == 1:
                pickup = input("\nWould you like to pick up " + room[i].items[0] + "? If so type in the name of the item you wish to pickup.")
            if len(room[i].items) == 2:
                if pickup == room[i].items[0] or pickup == room[i].items[1]:
                    if len(player.items) == 2:
                        drop = input("would you like to drop " + player.items[0] + " or " + player.items[1] + "?")
                        if drop == player.items[0] or drop == player.items[1]:
                            player.dropItem(drop)
                            room[i].addItem(drop)
            else:
                if pickup == room[i].items[0]:
                    if len(player.items) == 2:
                        drop = input("would you like to drop " + player.items[0] + " or " + player.items[1] + "?")
                        if drop == player.items[0] or drop == player.items[1]:
                            player.dropItem(drop)
                            room[i].addItem(drop)
            
            if pickup != '':
                if len(room[i].items) == 1 and pickup == room[i].items[0]:
                    player.addItem(pickup)
                    room[i].dropItem(pickup)
                elif len(room[i].items) == 2 and pickup == room[i].items[0] or pickup == room[i].items[1]:
                    player.addItem(pickup)
                    room[i].dropItem(pickup)
            #getattr 
            move = input("\n\nWould you like to move n, s, e, w?")
            if move == 'q' or move == 'quit':
                flag = False
            elif move == 'n':
                if hasattr(room[i], "n_to"):
                    player.changeRoom(room[i].n_to)
                else:
                    print("\n\n\nPick another direction. You can't go here.\n\n\n")
                    move
            elif move == 's':
                if hasattr(room[i], "s_to"):
                    player.changeRoom(room[i].s_to)
                else:
                    print("\n\n\nPick another direction. You can't go here.\n\n\n")
                    move
            elif move == 'e':
                if hasattr(room[i], "e_to"):
                    player.changeRoom(room[i].e_to)
                else:
                    print("\n\n\nPick another direction. You can't go here.\n\n\n")
                    move
            elif move == 'w':
                if hasattr(room[i], "w_to" ):
                    player.changeRoom(room[i].w_to)
                else:
                    print("\n\n\nPick another direction. You can't go here.\n\n\n")
                    move

# * Prints the current room name // 
# * Prints the current description (the textwrap module might be useful here). // 
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


# to change room call player.changeRoom(newRoom)