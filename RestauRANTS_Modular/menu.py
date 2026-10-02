"""Menu display."""

from config import SEPARATOR


def display_menu(menu):
    print(SEPARATOR)
    print("           FAST BITE DINER - MENU")
    print(SEPARATOR)
    for item_name, item_price in menu.items():
        print(f"{item_name:<20}Php {item_price:>8.2f}")
    print(SEPARATOR)
