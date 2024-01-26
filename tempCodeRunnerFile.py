
            weapon_to_get = next_move[1].title()
            current_weapon = Section[current_section]["Weapon"]

            if weapon_to_get == current_weapon:
                if len(inventory) <= 10:
                    if weapon_to_get in inventory:
                        inventory[weapon_to_get] += 1
                    else:
                        inventory[weapon_to_get] = 1
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

    #  #Player VS Monster

    # Activate Key and Win
    elif action == "A":
        # Check if the player is in the correct exit section and has the key
        if current_section == f"SECTION {correct_exit}" and "Key" in inventory:
            print("You have activated the key! You win!")
            break
        else:
            print("You can't activate the key here.")

    # Exit games
    elif action == "Exit":
        break

    else:
        msg = "Invalid command"
