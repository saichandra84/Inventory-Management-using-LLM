# inventory.py

class InventoryManager:
    def __init__(self):
        self.inventory = {
            "tshirts": 20,
            "pants": 15
        }

    def get_inventory(self):
        return self.inventory

    def update_inventory(self, item, change):
        item = item.lower()
        if item not in self.inventory:
            raise ValueError(f"Invalid item: {item}")
        self.inventory[item] += change
        return self.inventory
