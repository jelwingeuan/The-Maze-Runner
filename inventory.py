# User's Inventory max 10
inventory = []

# Track User's Section Location
current_section = "The Glade"

# User's Last Move
msg = ""

clear()
prompt()

##Game loop # stop==win lose or exit
while True:

    clear()

    print(f"{name}, you are in the {current_section}.\n Inventory: {inventory}\n{'-'*27}")

    #Display msg
    print(msg)

    #Weapon
    if "Weapon" in Section[current_section].keys():

        current_weapon = Section[current_section]["Weapon"]



        if current_weapon[-1] == 's':
            print(f"You see {current_weapon}")
            
        elif current_weapon[0] == 'a'or 'e'or'i'or 'o' or'u':
            print(f"You see an {current_weapon}")
            
        else:
            print(f"You see a {current_weapon}")

    class Weapon:
        def __init__(self, name, power):
            self.name = name
            self.power = power

    class Grenades(Weapon):
        def __init__(self):
            super().__init__(Grenades, 50)
    
    class Bow(Weapon):
        def __init__(self):
            super().__init__(Bow, 40)
    
    class Sword(Weapon):
        def __init__(self):
            super().__init__(Sword,30)
    
    class Spear(Weapon):
        def __init__(self):
            super().__init__(Spear, 20)

    class Darts(Weapon):
        def __init__(self):
            super().__init__(Darts, 10)

    class Player:
        def __init__(self, name, hp, weapon):
            self.name = name 
            self.hp= hp
            self.weapon = weapon

        def attack(self, monster):
            self.weapon.attack(monster)
        
    class Monster:
        def __init__(self,name, hp):
            self.name = name
            self.hp = hp

    # Monster
        
    # For movement
    player_input = input("Enter your move:\n")

    # Split move into words
    next_move = player_input.split(' ')

    # Action first word
    action = next_move[0].title()

    if len(next_move) > 1:
        weapon = next_move[1].title()
        direction = next_move[1].title()
        
    #Moving
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
            current_weapon = Section[current_section]["Weapon"]

            if weapon_to_get == current_weapon:
                if len(inventory)<= 10 :
                    if weapon_to_get in inventory:
                        inventory[weapon_to_get] += 1
                    else:
                        inventory[weapon_to_get]=1
                    msg = f"You got {weapon_to_get}! (There are now {inventory[weapon_to_get]} of them in your inventory.)"
                else:
                    msg = "Your inventory is full! "
            else:
                msg = "There's no such weapon here."
        except KeyError:
            msg = "There's no weapon in this section."
        except Exception as e:
            print(f"An error occurred: {e}")
            msg = "Something went wrong."
            
    #Exit game
    elif action == "Exit":
        break

    else:
        msg = "Invalid command"
