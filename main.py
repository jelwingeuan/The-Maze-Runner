import os
import random

from PIL import Image

map = Image.open("themazerunner.png")
map.show()

#Clears screen
def clear():
    os.system('cls' if os.name = 'nt' else 'clear')

# Menu
def prompt():
    print("\t\t\tWelcome To The Maze Runner Game\n\n")

    input("Press Any Key To Continue...")


# Maze Map
Section = {
    # Starting Point-----------------------------------
    "The Glade": {  # 4 Ways
        "North": "The Glade Entrance",
        "East": "Runners' Junction",
        "South": "Twilight Tunnels",
        "West": "Whispering Woods",
    },
    # 2nd Phase of the Maze----------------------------
    "The Glade Entrance": {  # 4 Ways
        "North": "Echoing Corridor",
        "East": "Shadow Labyrinth",
        "South": "The Glade",
        "West": "Grievers' Alley",
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
        "East": "Serpent's Spiral",
        "South": "Cryptic Crossroads",
        "West": "Twilight Tunnels",
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
    # 3rd Phase of the Maze-----------------------------
    "Echoing Corridor": {  # 3 Ways
        "North": "SECTION 5",
        "East": "Wraith's Walk",
        "South": "The Glade Entrance",
    },
    "Wraith's Walk": {  # 3 Ways
        "East": "Abyssal Arches",
        "South": "Shadow Labyrinth",
        "West": "Echoing Corridor",
    },
    "Abyssal Arches": {  # 1 Way
        "West": "Wraith's Walk",
    },
    "Eclipsed Enclave": {  # 3 Ways
        "East": "SECTION 3",
        "South": "Veiled Vista",
        "East": "Shawdow Labyrinth",
    },
    "Veiled Vista": {"North": "Eclipsed Enclave"},  # 1 Way
    "Serpent's Spiral": {  # 2 Ways
        "South": "Moonlit Maze",
        "East": "Enigma Passage",
    },
    "Moonlit Maze": {  # 2 Ways
        "North": "Serpent's Spiral",
        "East": "SECTION 8",
    },
    "Cryptic Crossroads": {  # 4 Ways
        "North": "Enigma Passage",
        "South": "SECTION 2",
    },
    "Enchanted Corridor": {  # 1 Way
        "West": "Starlit Sentries",
    },
    "Starlit Sentries": {  # 3 Ways
        "East": "Enchanted Corridor",
        "South": "SECTION 4",
        "West": "Celestial Circuit",
    },
    "Celestial Circuit": {  # 2 Ways
        "North": "Forgotten Nexus",
        "East": "Starlit Sentries",
    },
    "Forgetten Nexus": {  # 3 Ways
        "East": "Solutide Path",
        "South": "Celestial Circuit",
        "West": "SECTION 6",
    },
    "Nebula Nexus": {  # 1 Way
        "East": "Whispering Woods",
    },
    "Mazeheart Nexus": {  # 2 Ways
        "North": "Twilight Traverse",
        "West": "SECTION 7",
    },
    "Twilight Traverse": {  # 3 Ways
        "North": "SECTION 1",
        "East": "Vortex Vestibule",
        "South": "Mazeheart Nexus",
    },
    "Vortex Vestibule": {  # 2 Ways
        "South": "Grievers' Alley",
        "West": "Twilight Traverse",
    },
}

#User's Inventory
Inventory = []

#Track User's Section Location
current_section = "The Glade"

#User's Last Move
msg = ""

clear()
prompt()

#Loop
while True:
    clear()
    #User's Display
    print(f"You're currently at {current_section}n\Inventory:{Inventory}" )
    print(msg)