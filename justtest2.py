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


# Display game menu
def prompt():
    print(
        "\t\t\tWelcome To The Maze Runner Game\n\n"
        "Moves:\t'go {direction}'(travel North, South, East, or West)\n"
        "\t'get {item}' (add current weapon to inventory)\n\n"
    )
    input("Press Enter To Continue...")


# Maze Map
Section = {
    # Starting Point-----------------------------------
    "The Glade": {
        "North": "The Glade Entrance",
        "East": "Runners' Junction",
        "South": "Twilight Tunnels",
        "West": "Whispering Woods",
    },
    # 2nd Phase of the Maze----------------------------
    "The Glade Entrance": {
        "North": "Echoing Corridor",
        "East": "Shadow Labyrinth",
        "South": "The Glade",
        "West": "Grievers' Alley",
        "Weapon": "Spear",
    },
    "Shadow Labyrinth": {
        "North": "Wraith's Walk",
        "East": "Eclipsed Enclave",
        "West": "The Glade Entrance",
        "Weapon": "Grenades",
    },
    "Runners' Junction": {
        "South": "Enigma Passage",
        "West": "The Glade",
        "Weapon": "Sword",
    },
    "Enigma Passage": {
        "North": "Runners' Junction",
        "East": "Serpent's Spiral",
        "South": "Cryptic Crossroads",
        "West": "Twilight Tunnels",
        "Monster": "Grievers",
    },
    "Twilight Tunnels": {
        "North": "The Glade",
        "East": "Enigma Passage",
        "West": "Solitude Path",
        "Weapon": "Bow",
    },
    "Solitude Path": {
        "North": "Whispering Woods",
        "East": "Twilight Tunnels",
        "West": "Forgotten Nexus",
        "Weapon": "Spear",
    },
    "Whispering Woods": {
        "North": "Greivers' Alley",
        "East": "The Glade",
        "South": "Solitude Path",
        "West": "Nebula Nexus",
        "Weapon": "Grenades",
    },
    "Grievers' Alley": {
        "North": "Vortex Vestibule",
        "East": "The Glade Entrance",
        "South": "Whispering Woods",
        "Monster": "Grievers",
    },
    # 3rd Phase of the Maze-----------------------------
    "Echoing Corridor": {
        "North": "SECTION 5",
        "East": "Wraith's Walk",
        "South": "The Glade Entrance",
        "Weapon": "Bow",
    },
    "Wraith's Walk": {
        "East": "Abyssal Arches",
        "South": "Shadow Labyrinth",
        "West": "Echoing Corridor",
        "Monster": "Grievers",
    },
    "Abyssal Arches": {"West": "Wraith's Walk", "Weapon": "Darts"},
    "Eclipsed Enclave": {
        "East": "SECTION 3",
        "South": "Veiled Vista",
        "West": "Shadow Labyrinth",
        "Weapon": "Spear",
    },
    "Veiled Vista": {"North": "Eclipsed Enclave", "Weapon": "Darts"},
    "Serpent's Spiral": {
        "South": "Moonlit Maze",
        "West": "Enigma Passage",
        "Weapon": "Spear",
    },
    "Moonlit Maze": {
        "North": "Serpent's Spiral",
        "East": "SECTION 8",
        "Weapon": "Darts",
    },
    "Cryptic Crossroads": {
        "North": "Enigma Passage",
        "South": "SECTION 2",
        "Weapon": "Darts",
    },
    "Enchanted Corridor": {"West": "Starlit Sentries", "Weapon": "Spear"},
    "Starlit Sentries": {
        "East": "Enchanted Corridor",
        "South": "SECTION 4",
        "West": "Celestial Circuit",
        "Weapon": "Sword",
    },
    "Celestial Circuit": {
        "North": "Forgotten Nexus",
        "East": "Starlit Sentries",
        "Monster": "Grievers",
    },
    "Forgotten Nexus": {
        "East": "Solitude Path",
        "South": "Celestial Circuit",
        "West": "SECTION 6",
        "Weapon": "Bow",
    },
    "Nebula Nexus": {"East": "Whispering Woods", "Monster": "Grievers"},
    "Mazeheart Nexus": {
        "North": "Twilight Traverse",
        "West": "SECTION 7",
        "Weapon": "Sword",
    },
    "Twilight Traverse": {
        "North": "SECTION 1",
        "East": "Vortex Vestibule",
        "South": "Mazeheart Nexus",
        "Weapon": "Darts",
    },
    "Vortex Vestibule": {
        "South": "Grievers' Alley",
        "West": "Twilight Traverse",
        "Weapon": "Sword",
    },
    # Exit Sections--------------------------------
    "SECTION 1": {"South": "Twilight Traverse"},
    "SECTION 2": {"North": "Cryptic Crossroads"},
    "SECTION 3": {"West": "Eclipsed Enclave"},
    "SECTION 4": {"North": "Starlit Sentries"},
    "SECTION 5": {"South": "Echoing Corridor"},
    "SECTION 6": {"East": "Forgotten Nexus"},
    "SECTION 7": {"East": "Mazeheart Nexus"},
    "SECTION 8": {"West": "Moonlit Maze"},
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
        super().__init__("Grenades", 50)


class Bow(Weapon):
    def __init__(self):
        super().__init__("Bow", 40)


class Sword(Weapon):
    def __init__(self):
        super().__init__("Sword", 30)


class Spear(Weapon):
    def __init__(self):
        super().__init__("Spear", 20)


class Darts(Weapon):
    def __init__(self):
        super().__init__("Darts", 10)


# Monster class
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health


# Function to handle player attacking monster
def player_attack_monster():
    global player_health

    monster = current_monsters[current_section]

    while monster["health"] > 0 and player_health > 0:
        print(f"You have encountered {monster['name']}! Prepare for battle.")
        print(f"You are fighting {monster['name']} (Health: {monster['health']})")
        print(f"Your health: {player_health}")

        if not inventory:
            print("You don't have any weapons to fight back! You have been defeated!")
            return True  # Indicate that the player has been defeated

        # Allow the player to choose a weapon from the inventory using numbers
        while True:
            print(
                "Please choose your weapon from your inventory by entering the corresponding number:"
            )
            index = 1
            for weapon_name, count in inventory.items():
                print(f"{index}. {weapon_name} ({count})")
                index += 1

            # Convert the input to an integer to select the weapon by index
            weapon_choice_index = input(
                "Enter the number of the weapon you want to use: "
            ).strip()

            # Check if the input is a valid integer
            if weapon_choice_index.isdigit():
                weapon_choice_index = int(weapon_choice_index)
                if 1 <= weapon_choice_index <= len(inventory):
                    weapon_choice = list(inventory.keys())[weapon_choice_index - 1]
                    break  # Exit the loop when a valid choice is made
                else:
                    print(
                        "Invalid weapon number. Please choose a valid number from the available options."
                    )
            else:
                print("Invalid input. Please enter a number.")

        # Now you have the selected weapon_choice as the weapon to use for the attack

        # Check if the player has been defeated
        if player_health <= 0:
            print("Your health dropped to 0! Game over.")
            return True  # Indicate that the player has been defeated

        # Further logic for attacking the monster goes here

        return False  # Indicate that the player hasn't been defeated yet


# Display game menu
clear()
prompt()

name = input("Please enter you name: ")

# Game loop
while True:
    clear()
    print(f"{name}, you are in the {current_section}.\nInventory: ", end="")

    # Display inventory
    if inventory:
        inventory_str = ", ".join(
            [f"{item}({count})" for item, count in inventory.items()]
        )
        print(inventory_str)
    else:
        print("Empty")

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
        current_weapon[-1] == "s"
        print(f"You see {current_weapon}")

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
            weapon_to_get = next_move[1].title()

            if weapon_to_get in inventory:
                inventory[weapon_to_get] += 1
            else:
                inventory[weapon_to_get] = 1  # Store the count of the item

            msg = f"You got {weapon_to_get}! (There are now {inventory[weapon_to_get]} of them in your inventory.)"
        except KeyError:
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
