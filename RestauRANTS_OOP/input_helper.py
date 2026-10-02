"""InputHelper class: validated user input."""


class InputHelper:
    @staticmethod
    def ask_yes_no(question):
        while True:
            answer = input(f"{question} (Y/N): ").strip().lower()
            if answer in ("y", "yes"):
                return True
            elif answer in ("n", "no"):
                return False
            else:
                print("Invalid input. Please type Y or N.")

    @staticmethod
    def get_valid_quantity():
        while True:
            raw_quantity = input("Enter quantity: ").strip()
            if raw_quantity.isdigit() and int(raw_quantity) > 0:
                return int(raw_quantity)
            print("Invalid quantity. Please enter a whole number greater than 0.")
