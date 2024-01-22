import random


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.items = []

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Items: ", ", ".join(self.items))


class Maze:
    def __init__(self):
        self.current_location = (0, 0)
        self.exit_location = (4, 4)

    def move(self, direction):
        x, y = self.current_location
        if direction == "N":
            y -= 1
        elif direction == "S":
            y += 1
        elif direction == "E":
            x += 1
        elif direction == "W":
            x -= 1
        self.current_location = (x, y)

    def is_at_exit(self):
        return self.current_location == self.exit_location


def print_intro():
    print("Welcome to the Maze Runner Game!")
    print("Your goal is to find the exit of the maze.\n")


def explore_maze(player, maze):
    directions = ["N", "S", "E", "W"]
    random.shuffle(directions)

    print("You find yourself in a maze. Choose a direction to explore:")

    for direction in directions:
        print(f"{direction} - {get_direction_description(direction)}")

    choice = input("Enter your choice (N/S/E/W): ").upper()

    if choice in directions:
        maze.move(choice)
        encounter_challenge(player)
    else:
        print("Invalid choice. Try again.")


def get_direction_description(direction):
    if direction == "N":
        return "North"
    elif direction == "S":
        return "South"
    elif direction == "E":
        return "East"
    elif direction == "W":
        return "West"


def encounter_challenge(player):
    chance = random.randint(1, 10)

    if chance <= 5:
        print("You encounter a challenge but manage to overcome it.")
    else:
        print("Oh no! You face a dangerous obstacle.")
        player.take_damage(random.randint(10, 20))
        print(f"You lose health. Your current health: {player.health}")


def main():
    print_intro()
    player_name = input("Enter your name: ")
    player = Player(player_name)
    maze = Maze()

    while player.is_alive() and not maze.is_at_exit():
        player.display_status()
        explore_maze(player, maze)

    if maze.is_at_exit():
        print(
            "Congratulations! You have found the exit of the maze and completed the game."
        )
    else:
        print("Game over! Your journey in the maze has come to an end.")


if __name__ == "__main__":
    main()
