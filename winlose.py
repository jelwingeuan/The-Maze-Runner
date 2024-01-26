class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.inventory = []

    def pick_up_weapon(self, weapon):
        self.inventory.append(weapon)

    def attack(self, monster, weapon):
        # Calculate damage based on the weapon's power
        damage = weapon.power
        # Deduct monster's HP
        monster.hp -= damage

    def take_damage(self, damage):
        self.hp -= damage


class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, player):
        # Deduct player's HP
        player.take_damage(self.damage)


# Create player and monster instances
player = Player("Player1", 100)
monster = Monster("Griever", 100, 10)  # Assuming monster does 10 damage per attack

# Assume the player has a list of weapons in their inventory
# Example weapons
sword = Weapon("Sword", 30)
bow = Weapon("Bow", 40)

# Player picks a weapon from inventory
selected_weapon = None
while selected_weapon not in player.inventory:
    print("Choose a weapon from your inventory:")
    for index, weapon in enumerate(player.inventory):
        print(f"{index + 1}. {weapon.name}")
    choice = input("Enter the number of the weapon: ")
    try:
        choice = int(choice)
        if 0 < choice <= len(player.inventory):
            selected_weapon = player.inventory[choice - 1]
        else:
            print("Invalid choice. Please select a valid weapon.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Player engages in combat with the monster
player.attack(monster, selected_weapon)
print(f"{player.name} attacks {monster.name} with {selected_weapon.name}!")

# Monster retaliates
monster.attack(player)
print(f"{monster.name} attacks {player.name}!")

# Check win/lose conditions
if player.hp <= 0:
    print("Game Over! You lose.")
elif monster.hp <= 0:
    print("Congratulations! You defeated the monster.")
