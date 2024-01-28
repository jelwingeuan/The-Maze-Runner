
# Allow the player to choose a weapon from the inventory
def choose_weapon_from_inventory():
    print("Please choose your weapon from your inventory:")
    for weapon_name in inventory.keys():
        print(f"- {weapon_name}")

    weapon_choice = (
        input("Enter the name of the weapon you want to use: ").strip().title()
    )

    # Check if the entered weapon name is in the inventory
    if weapon_choice in inventory:
        return weapon_choice
    else:
        print("Invalid weapon name. Please choose from the available options.")
        return None


# Function to handle player attacking monster
def player_attack_monster(weapon_choice):
    global player_health

    monster = current_monsters[current_section]

    if not weapon_choice:
        print("You need to choose a weapon to attack!")
        return False

    weapon_instance = inventory[weapon_choice]

    # Check if the weapon_instance is an instance of a weapon object
    if isinstance(weapon_instance, Weapon):
        power = weapon_instance.power
        monster["health"] -= power
        print(f"You attacked with {weapon_choice} and dealt {power} damage!")

        # Remove the used weapon from inventory
        if isinstance(inventory[weapon_choice], int):
            del inventory[weapon_choice]
        else:
            inventory[weapon_choice] -= 1

        player_health -= 10  # Reduce player's health by a fixed amount
        print("Monster retaliated and dealt 10 damage to you!")
        return True
    else:
        print("Invalid weapon selection. Please choose a valid weapon.")
        return False


# Game loop
while True:
    clear()
    print(f"{__name__}, you are in the {current_section}.\nInventory: ", end="")

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