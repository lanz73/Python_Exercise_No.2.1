"""Functions that ask the user for input and validate it."""


def ask_yes_no(question):
    while True:
        answer = input(f"{question} (Y/N): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("Invalid input. Please type Y or N.")


def get_valid_menu_item(menu):
    while True:
        chosen_item = input("Enter menu item: ").strip()
        for menu_item in menu:
            if menu_item.lower() == chosen_item.lower():
                return menu_item
        print("Item not found on the menu. Please check spelling and try again.")


def get_valid_quantity():
    while True:
        raw_quantity = input("Enter quantity: ").strip()
        if raw_quantity.isdigit() and int(raw_quantity) > 0:
            return int(raw_quantity)
        print("Invalid quantity. Please enter a whole number greater than 0.")
