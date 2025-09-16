
class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            return True
        else:
            return False

    def take_item(self, item_name):
        item = self.current_room.get_item(item_name)
        if item:
            self.inventory.append(item)
            return item
        return None

    def get_inventory(self):
        if not self.inventory:
            return "You are not carrying anything."
        return "You are carrying: " + ", ".join(item.name for item in self.inventory)
