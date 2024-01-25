# User's Inventory max 10
inventory = []

# Track User's Section Location
current_section = "The Glade"

# User's Last Move
msg = ""

clear()
prompt()

#Game loop # stop==win lose or exit
while True:

    clear()

    print(f"You are in the {current_section}\n Inventory: {inventory}\n{'-'*27}")

    #Display msg
    print(msg)

    #Weapon
    if "Weapon" in Section[current_section].keys():

        current_weapon = Section[current_section]["Weapon"]

        if current_weapon not in inventory:

            if current_weapon[-1] == 's':
                print(f"You see {current_weapon}")
            
            elif current_weapon[0] == 'a'or 'e'or'i'or 'o' or'u':
                print(f"You see an {current_weapon}")
            
            else:
                print(f"You see a {current_weapon}")


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
            if weapon == Section[current_section]["Weapon"]:

                if weapon not in inventory:
                    inventory.append(Section[current_section]["Weapon"])
                    msg = f"You got {weapon}!"

                ###
                else:
                    msg = f"You already have the {weapon}."
                
            else:
                msg = "You meet Monster!"

        except:
            msg = "You meet Monster!"

    #Exit game
    elif action == "Exit":
        break

    else:
        msg = "Invalid command"

if {weapon} > 10:
        print(f"No more space to get {current_weapon}. Is time to attack Monster！ ")
            

            



    





        
                
    
                

                
    

            

        


