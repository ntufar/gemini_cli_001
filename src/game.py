
from room import Room
from player import Player
from item import Item
from character import Character

class Game:
    def __init__(self):
        self.create_world()
        self.player = Player(self.starting_room)
        self.game_over = False

    def create_world(self):
        # Create rooms
        self.starting_room = Room("Starting Room", "You are in a small, dimly lit room. There is a door to the north.")
        kitchen = Room("Kitchen", "You are in a kitchen. There are doors to the south and east.")
        garden = Room("Garden", "You are in a beautiful garden. There is a path to the west and a door to the north.")
        library = Room("Library", "You are in a dusty library. There is a door to the south.")
        self.locked_hallway = Room("Locked Hallway", "You are in a long, dark hallway. A ghostly figure floats in the air.")

        # Create items
        key = Item("Key", "A small, rusty key.")
        shovel = Item("Shovel", "A sturdy shovel.")
        amulet = Item("Amulet", "A strange, glowing amulet.")
        self.treasure = Item("Treasure", "A chest full of gold and jewels!")

        # Create characters
        ghost = Character("Ghost", "A translucent figure of an old man.", "The treasure is buried where the sun shines brightest.")

        # Add exits
        self.starting_room.add_exit("north", self.locked_hallway)
        self.locked_hallway.add_exit("south", self.starting_room)
        kitchen.add_exit("south", self.starting_room)
        kitchen.add_exit("east", garden)
        garden.add_exit("west", kitchen)
        garden.add_exit("north", library)
        library.add_exit("south", garden)

        # Add items to rooms
        kitchen.add_item(key)
        garden.add_item(shovel)
        library.add_item(amulet)

        # Add characters to rooms
        self.locked_hallway.character = ghost

    def play(self):
        while not self.game_over:
            print("\n" + "-" * 20)
            print(self.player.current_room.name)
            print(self.player.current_room.description)

            if hasattr(self.player.current_room, 'character'):
                print(f"You see a {self.player.current_room.character.name}.")

            if self.player.current_room.items:
                print("You see: " + ", ".join(item.name for item in self.player.current_room.items))

            command = input("> ").lower().split()

            if not command:
                continue

            action = command[0]

            if action == "quit":
                print("Thanks for playing!")
                break
            elif action == "go":
                self.handle_go(command)
            elif action == "take":
                self.handle_take(command)
            elif action == "inventory":
                print(self.player.get_inventory())
            elif action == "dig":
                self.handle_dig()
            elif action == "talk":
                self.handle_talk()
            else:
                print("I don't understand that command.")

    def handle_go(self, command):
        if len(command) > 1:
            direction = command[1]
            if self.player.current_room == self.starting_room and direction == "north":
                if any(item.name == "Key" for item in self.player.inventory):
                    if self.player.move(direction):
                        print(f"You unlock the door and go {direction}.")
                else:
                    print("The door is locked.")
            elif self.player.move(direction):
                print(f"You go {direction}.")
            else:
                print("You can't go that way.")
        else:
            print("Go where?")

    def handle_take(self, command):
        if len(command) > 1:
            item_name = command[1]
            item = self.player.take_item(item_name)
            if item:
                print(f"You take the {item.name}.")
                if item == self.treasure:
                    print("Congratulations! You found the treasure! You win!")
                    self.game_over = True
            else:
                print("You don't see that here.")
        else:
            print("Take what?")

    def handle_dig(self):
        if self.player.current_room.name == "Garden":
            if any(item.name == "Shovel" for item in self.player.inventory):
                print("You dig a hole and find a hidden treasure chest!")
                self.player.current_room.add_item(self.treasure)
            else:
                print("You have nothing to dig with.")
        else:
            print("You can't dig here.")

    def handle_talk(self):
        if hasattr(self.player.current_room, 'character'):
            if any(item.name == "Amulet" for item in self.player.inventory):
                print(f'The {self.player.current_room.character.name} says: "{self.player.current_room.character.dialogue}"')
            else:
                print(f"The {self.player.current_room.character.name} seems to ignore you.")
        else:
            print("There is no one to talk to.")

if __name__ == "__main__":
    game = Game()
    game.play()
