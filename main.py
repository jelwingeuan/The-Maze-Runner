import os


# Menu
def prompt():
    print("\t\t\tWelcome To The Maze Runner Game\n\n")

    input("Press Any Key To Continue...")


# Maze Map
Section = {
    # Starting Point
    "The Glade": {  # 4 Ways
        "North": "The Glade Entrance",
        "East": "Runners' Junction",
        "South": "Twilight Tunnels",
        "West": "Whispering Woods",
    },
    # 2nd Phase of the Maze
    "The Glade Entrance": {  # 4 Ways
        "North": "Echoing Corridor",
        "East": "Shadow Labyrinth",
        "South": "The Glade",
        "West": "Grivers' Alley",
    },
    "Shadow Labyrinth": {  # 3 Ways
        "North": "Wraith's Walk",
        "East": "Eclipsed Enclave",
        "West": "The Glade Entrance",
    },
    "Runner' Junction": {  # 2 Ways
        "South": "Enigma Passage",
        "West": "The Glade",
    },
    "Enigma Passage": {  # 4 Ways
        "North": "Runners' Junction",
        "East": "Runners' Junction",
        "South": "Twilight Tunnels",
        "West": "Whispering Woods",
    },
    "Twilight Tunnels": {  # 3 Ways
        "North": "The Glade",
        "East": "Enigma Passage",
        "West": "Solitude Path",
    },
    "Solitude Path": {  # 3 Ways
        "North": "Whispering Woods",
        "East": "Twilight Tunnels",
        "West": "Forgotten Nexus",
    },
    "Whispering Woods": {  # 4 Ways
        "North": "Grivers' Alley",
        "East": "The Glade",
        "South": "Solitude Path",
        "East": "Nebula Nexus",
    },
    "Grivers' Alley": {  # 3 Ways
        "North": "Vortex Vestibule",
        "East": "The Glade Entrance",
        "South": "Whispering Woods",
    },
    # 3rd Phase of the Maze
    "Echoing Corridor": {  #3 Ways 
        "North": "SECTION 5",
        "East": "Wraith's Walk",
        "South": "The Glade Entrance",
    },
}
