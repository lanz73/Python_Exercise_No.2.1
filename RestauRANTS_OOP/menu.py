"""Menu class: holds the items and their prices."""

from config import SEPARATOR


class Menu:
    def __init__(self, items):
        self.items = items

    def display(self):
        print(SEPARATOR)
        print("           FAST BITE DINER - MENU")
        print(SEPARATOR)
        for item_name, item_price in self.items.items():
            print(f"{item_name:<20}Php {item_price:>8.2f}")
        print(SEPARATOR)

    def find_item(self, chosen_item):
        """Return the properly-cased menu name, or None if not found."""
        for menu_item in self.items:
            if menu_item.lower() == chosen_item.lower():
                return menu_item
        return None

    def get_price(self, item_name):
        return self.items[item_name]

    def ask_for_item(self):
        while True:
            chosen_item = input("Enter menu item: ").strip()
            found = self.find_item(chosen_item)
            if found is not None:
                return found
            print("Item not found on the menu. Please check spelling and try again.")
