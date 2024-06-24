import os
import random
from PIL import Image


# Clears screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Display difficulty menu
def difficulty_menu():
    clear()
    print(
        "\t\t\tChoose Difficulty Level\n\n" "\t1. Easy\n" "\t2. Normal\n" "\t3. Hard\n"
    )
    choice = input("Enter your choice (1-3): ")
    return choice


# Load and display PNG image
def display_map(difficulty):
    map_files = {
        "1": "themazerunnermapeasy.png",
        "2": "themazerunnermapnormal.png",
        "3": "themazerunnermaphard.png",
    }
    map_file = map_files.get(difficulty)
    if map_file:
        img = Image.open(map_file)
        img.show()
    else:
        print("Invalid difficulty level.")


# Difficulty level selection
choice = difficulty_menu()

# Display corresponding map based on difficulty level
display_map(choice)


# Menu
def prompt():
    print(
        "\t\t\tWelcome To The Maze Runner Game\n\n\
        Moves:\t'go {direction}'(travel North, South, East, or West)\n\
        \t'get {item}' (add current weapon to inventory)\n\n"
    )

    input("Press Enter To Continue...")


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
        "Weapon": "Spear",
    },
    "Shadow Labyrinth": {  # 3 Ways
        "North": "Wraith's Walk",
        "East": "Eclipsed Enclave",
        "West": "The Glade Entrance",
        "Weapon": "Grenades",
    },
    "Runners' Junction": {  # 2 Ways
        "South": "Enigma Passage",
        "West": "The Glade",
        "Weapon": "Sword",
    },
    "Enigma Passage": {  # 4 Ways
        "North": "Runners' Junction",
        "East": "Serpent's Spiral",
        "South": "Cryptic Crossroads",
        "West": "Twilight Tunnels",
        "Monster": "Grievers",
    },
    "Twilight Tunnels": {  # 3 Ways
        "North": "The Glade",
        "East": "Enigma Passage",
        "West": "Solitude Path",
        "Weapon": "Bow",
    },
    "Solitude Path": {  # 3 Ways
        "North": "Whispering Woods",
        "East": "Twilight Tunnels",
        "West": "Forgotten Nexus",
        "Weapon": "Spear",
    },
    "Whispering Woods": {  # 4 Ways
        "North": "Grievers' Alley",
        "East": "The Glade",
        "South": "Solitude Path",
        "West": "Nebula Nexus",
        "Weapon": "Grenades",
    },
    "Grievers' Alley": {  # 3 Ways
        "North": "Vortex Vestibule",
        "East": "The Glade Entrance",
        "South": "Whispering Woods",
        "Monster": "Grievers",
    },
    # 3rd Phase of the Maze-----------------------------
    "Echoing Corridor": {  # 3 Ways
        "North": "SECTION 5",
        "East": "Wraith's Walk",
        "South": "The Glade Entrance",
        "Weapon": "Bow",
    },
    "Wraith's Walk": {  # 3 Ways
        "East": "Abyssal Arches",
        "South": "Shadow Labyrinth",
        "West": "Echoing Corridor",
        "Monster": "Grievers",
    },
    "Abyssal Arches": {"West": "Wraith's Walk", "Weapon": "Darts"},  # 1 Way
    "Eclipsed Enclave": {  # 3 Ways
        "East": "SECTION 3",
        "South": "Veiled Vista",
        "West": "Shadow Labyrinth",
        "Weapon": "Spear",
    },
    "Veiled Vista": {"North": "Eclipsed Enclave", "Weapon": "Darts"},  # 1 Way
    "Serpent's Spiral": {  # 2 Ways
        "South": "Moonlit Maze",
        "West": "Enigma Passage",
        "Weapon": "Spear",
    },
    "Moonlit Maze": {  # 2 Ways
        "North": "Serpent's Spiral",
        "East": "SECTION 8",
        "Weapon": "Darts",
    },
    "Cryptic Crossroads": {  # 4 Ways
        "North": "Enigma Passage",
        "South": "SECTION 2",
        "Weapon": "Darts",
    },
    "Enchanted Corridor": {"West": "Starlit Sentries", "Weapon": "Spear"},  # 1 Way
    "Starlit Sentries": {  # 3 Ways
        "East": "Enchanted Corridor",
        "South": "SECTION 4",
        "West": "Celestial Circuit",
        "Weapon": "Sword",
    },
    "Celestial Circuit": {  # 2 Ways
        "North": "Forgotten Nexus",
        "East": "Starlit Sentries",
        "Monster": "Grievers",
    },
    "Forgotten Nexus": {  # 3 Ways
        "East": "Solitude Path",
        "South": "Celestial Circuit",
        "West": "SECTION 6",
        "Weapon": "Bow",
    },
    "Nebula Nexus": {"East": "Whispering Woods", "Monster": "Grievers"},  # 1 Way
    "Mazeheart Nexus": {  # 2 Ways
        "North": "Twilight Traverse",
        "West": "SECTION 7",
        "Weapon": "Sword",
    },
    "Twilight Traverse": {  # 3 Ways
        "North": "SECTION 1",
        "East": "Vortex Vestibule",
        "South": "Mazeheart Nexus",
        "Weapon": "Darts",
    },
    "Vortex Vestibule": {  # 2 Ways
        "South": "Grievers' Alley",
        "West": "Twilight Traverse",
        "Weapon": "Sword",
    },
    # Exit Sections--------------------------------
    "SECTION 1": {
        "South": "Twilight Traverse",
    },
    "SECTION 2": {
        "North": "Cryptic Crossroads",
    },
    "SECTION 3": {
        "West": "Eclipsed Enclave",
    },
    "SECTION 4": {
        "North": "Starlit Sentries",
    },
    "SECTION 5": {
        "South": "Echoing Corridor",
    },
    "SECTION 6": {
        "East": "Forgotten Nexus",
    },
    "SECTION 7": {
        "East": "Mazeheart Nexus",
    },
    "SECTION 8": {
        "West": "Moonlit Maze",
    },
}


# User's Inventory with a maximum capacity of 10
inventory = {}


# Function to randomize exit sections
def get_random_exit_section():
    return random.randint(1, 8)


# Track User's Section Location
current_section = "The Glade"

# User's Last Move
msg = ""

# Vowels
vowels = ["a", "e", "i", "o", "u"]


# Display game menu
clear()
prompt()

name = input("Please enter you name: ")

# Define correct_exit outside the loop initially
correct_exit = None

# Player health and monster objects
player_health = 100
current_monsters = {
    "Enigma Passage": {"name": "Grievers", "health": 100},
    "Grievers' Alley": {"name": "Grievers", "health": 100},
    "Wraith's Walk": {"name": "Grievers", "health": 100},
    "Celestial Circuit": {"name": "Grievers", "health": 100},
    "Nebula Nexus": {"name": "Grievers", "health": 100},
}


# Weapons
class Weapon:
    def __init__(self, name, power):
        self.name = name
        self.power = power


class Grenades(Weapon):
    def __init__(self):
        super().__init__("Grenades", 40)


class Bow(Weapon):
    def __init__(self):
        super().__init__("Bow", 30)


class Sword(Weapon):
    def __init__(self):
        super().__init__("Sword", 20)


class Spear(Weapon):
    def __init__(self):
        super().__init__("Spear", 10)


class Darts(Weapon):
    def __init__(self):
        super().__init__("Darts", 5)


# Monster class
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health


# Function to handle player attacking monster
def player_attack_monster():
    global player_health
    monster = current_monsters[current_section]

    # Check if the player has weapons to fight back
    if not inventory:
        print("You don't have any weapons to fight back! You have been defeated!")
        return True

    while monster["health"] > 0 and player_health > 0:
        print(f"You have encountered {monster['name']}! Prepare for battle.")
        print(f"You are fighting {monster['name']} (Health: {monster['health']})")
        print(f"Your health: {player_health}")

        while True:
            print("Please choose your weapon: ")
            for weapon_name, weapon_instance in inventory.items():
                print(f"{weapon_name} (Power: {weapon_instance.power})")

            weapon_choice = input("Please enter your choice: ")
            if weapon_choice in inventory:
                break
            else:
                print("Invalid weapon choice.")

        weapon_instance = inventory[weapon_choice]
        power = weapon_instance.power
        monster["health"] -= power
        print(f"You attacked with {weapon_choice} and output {power} damage! ")

        # Monster retaliation
        player_health -= 20  # Reduce player's health by a fixed amount
        print("Monster retaliated and dealt 20 damage to you!")

    # Check if the player has been defeated
    if player_health <= 0:
        print("Your health dropped to 0! Game over.")
        return True  # Indicate that the player has been defeated

    # If the monster has been defeated
    if monster["health"] <= 0:
        print(
            f"You defeated the {monster['name']}! Now continue search for exit section."
        )
        return False  # Indicate that the player defeated the monster and can continue the game


# Game loop # stop==win lose or exit
while True:
    clear()

    # Inventory display
    if inventory:
        inventory_str = ", ".join(inventory.keys())
        print(f"Inventory: {inventory_str}")
    else:
        print("Inventory: Empty")

    print(f"{name}, you are in the {current_section}.\n{'-'*27}")

    # Display msg
    print(msg)

    # Key Cursor
    if current_section == "The Glade" and correct_exit is None:
        correct_exit = get_random_exit_section()

    # Print the correct exit section for the key cursor
    if correct_exit is not None:
        print(f"The correct exit for the key is SECTION {correct_exit}")

    # Check if the player has reached the correct exit section
    if current_section == f"SECTION {correct_exit}":
        print("You have reached the correct exit section.")

        # Player activates the key cursor
        activation_key = input("Press 'a' to activate the key cursor: ").lower()
        if activation_key == "a":
            print(
                "Congratulations! You have activated the key cursor. You've escaped the maze"
            )
            break
            # Game win condition or any other actions after winning

    # Check if the current section has a monster
    print(f"Current Section: {current_section}")
    if current_section in current_monsters:
        print("Monster encountered!")
        if player_attack_monster():  # Check if the player has been defeated
            break  # End the game if the player is defeated
    else:
        print("No monster in this section")

    # End the game if the player is defeated and has no weapons
    if player_health <= 0:
        print("Your health dropped to 0! Game over.")
        break

    # Weapon Indicator
    if "Weapon" in Section[current_section].keys():
        current_weapon = Section[current_section]["Weapon"]

        if current_weapon[-1] == "s":
            print(f"You see {current_weapon}")

        elif current_weapon[0] in vowels:
            print(f"You see an {current_weapon}")

        else:
            print(f"You see a {current_weapon}")

    # For movement
    player_input = input("Enter your move:\n")

    # Split move into words
    next_move = player_input.split(" ")

    # Action first word
    action = next_move[0].title()

    if len(next_move) > 1:
        weapon = next_move[1].title()
        direction = next_move[1].title()

    # Moving
    if action == "Go":
        try:
            current_section = Section[current_section][direction]
            msg = f"You travel {direction}."

        except:
            msg = f"You can't go that way."

    # Picking
    elif action == "Get":
        try:
            # Check if there is a Weapon key in the current section
            if "Weapon" in Section[current_section]:
                weapon_to_get = Section[current_section]["Weapon"].title()

                # Check if the weapon to get matches the weapon in the section
                if weapon_to_get == weapon.title():
                    # Create an instance of the weapon based on its name
                    if weapon_to_get == "Grenades":
                        weapon_instance = Grenades()
                    elif weapon_to_get == "Bow":
                        weapon_instance = Bow()
                    elif weapon_to_get == "Sword":
                        weapon_instance = Sword()
                    elif weapon_to_get == "Spear":
                        weapon_instance = Spear()
                    elif weapon_to_get == "Darts":
                        weapon_instance = Darts()
                    else:
                        raise ValueError("Invalid weapon type")

                    # Add the weapon to the inventory
                    if len(inventory) >= 0:
                        if weapon_to_get in inventory:
                            inventory[weapon_to_get] += 1
                        else:
                            inventory[weapon_to_get] = weapon_instance
                        msg = f"You got {weapon_to_get}!"
                    else:
                        msg = "Your inventory is full! "
                else:
                    msg = f"There's no {weapon} in this section."
            else:
                msg = "There's no weapon in this section."
        except Exception as e:
            print(f"An error occurred: {e}")
            msg = "Something went wrong."

    # Attack
    elif action == "Attack":
        if current_section in current_monsters:
            if current_monsters[current_section]["name"] == "Grievers":
                print("You met the boss! It's time to attack the monster!")
                player_attack_monster()
            else:
                print("There's no monster to attack in this section.")

    # Exit games
    elif action == "Exit":
        break

    else:
        msg = "Invalid command"
