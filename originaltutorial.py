# Original Tutorial Code
# Tutorial: "Text Based Dungeon Game in Python | Coding Tutorial"
# Author:  dante0527
# Tutorial Link: https://www.youtube.com/watch?v=lI6S2-icPHE&t=301s (youtube) & https://github.com/dante0527/TextBasedGame (github)

# This file contains the original code obtained from the tutorial mentioned above.
# It serves as the starting point for my assignment, where I'll be adding new features
# and making modifications to create a unique text-based maze runner game.
# Modifications will be made in a separate file named 'main.py'.

# Original Tutorial Code Starts Here: (The code it's kinda washed up when take it from git repo)


# import os

# from PIL import Image                                                                                
# img = Image.open('ShadowGameMap.png')
# img = Image.open('Map.png')
# img.show() 


# @@ -116,7 +116,7 @@ def prompt():
#     #           add item to inventory
#     elif action == 'get':
#         try:
#             if object in rooms[current_room].values():
#             if object in rooms[current_room]["Item"]:

#                 if object not in inventory:

# @@ -128,9 +128,8 @@ def prompt():

#             else:
#                 print(f"Can't find {object}.")

#         except:
#             print("You can't get that item")
#             print(f"Can't find {object}")

#     # Exit command breaks while-loop and terminates program
#     elif action == 'exit':

#     elif action == "Get":
#         try:
#             if item == rooms[current_room]["Item"]:

#         if item == rooms[current_room]["Item"]:

#             if item not in inventory:
#                 if item not in inventory:

#                 inventory.append(rooms[current_room]["Item"])
#                 msg = f"{item} retrieved!"
#                     inventory.append(rooms[current_room]["Item"])
#                     msg = f"{item} retrieved!"

#                 else:
#                     msg = f"You already have the {item}"

#             else:
#                 msg = f"You already have the {item}"

#         else:
#                 msg = f"Can't find {item}"
#         except:
#             msg = f"Can't find {item}"


#     # Exit program
#     elif action == "Exit":