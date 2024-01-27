#Grenades = 50% 
#Bow = 40% 
#Sword = 30% 
#Spear = 20% 
#Darts = 10%  


# Weapon Indicator    
if "Weapon" in Section[current_section].keys():
    current_weapon = Section[current_section]["Weapon"]

    if current_weapon[-1] == "s":
        print(f"You see {current_weapon}")

    elif current_weapon[0] == "a" or "e" or "i" or "o" or "u":
        print(f"You see an {current_weapon}")

    else:
        print(f"You see a {current_weapon}")

# Monster
class Monster:
    def __init__(self,name, health):
        self.name = name
        self.health = health

current_monsters = {
    "Enigma Passage": Monster("Grievers",100),
    "Grievers' Alley": Monster("Grievers",100),
    "Wraith's Walk": Monster("Grievers",100),
    "Celestial Circuit": Monster("Grievers",100),
    "Nebula Nexus": Monster("Grievers",100)
}

player_health = 100

# Player attack monster
def player_attack_monster():
    global player_health
    monster = current_monsters[current_section]

    while monster.health > 0 and player_health > 0:
        print(f"You have encountered {monster.name}! Prepare for battle.")
        print(f"You are fighting {monster.name} (Health: {monster.health}% )")
        print(f"Your health: {player_health}% ")

        if not inventory: #player didn't have any weapons
            print("You don't have any weapons to fight back! You have been defeated!")
            break

        while True:
            print("Please choose your weapon: ")
            for weapon_name, weapon in inventory.items:
                print(f"{weapon_name} (Power: {weapon.power}%)")

            weapon_choice = input("Please enter your choice: ")
            if weapon_choice in inventory:
                break # have weapon to choose
            else:
                print("Invalid weapon choice.")

        weapon = inventory[weapon_choice]
        power = weapon.power
        monster.health -= power
        print(f"You attacked with {weapon_name} and output {power}% damage! ")

        # Monster will retaliate after player attack it
        player_health -= 10
        print("Monster retaliated and dealth 10% damage to you!")