"""Fast Bite Diner - Python OOP version. Run this file."""

from config import MENU
from input_helper import InputHelper
from menu import Menu
from order import Order
from receipt import Receipt


class FastBiteDiner:
    def __init__(self):
        self.menu = Menu(MENU)

    def take_orders(self):
        order = Order()
        while True:
            item_name = self.menu.ask_for_item()
            quantity = InputHelper.get_valid_quantity()
            order.add_item(item_name, self.menu.get_price(item_name), quantity)
            if not InputHelper.ask_yes_no("Order another item?"):
                break
        return order

    def run(self):
        self.menu.display()

        if not InputHelper.ask_yes_no("Would you like to place an order?"):
            print("Thank you for visiting Fast Bite Diner. Goodbye!")
            return

        order = self.take_orders()
        is_senior_or_pwd = InputHelper.ask_yes_no("Are you a Senior Citizen or PWD?")
        discount_amount, discount_label = order.get_discount(is_senior_or_pwd)
        Receipt(order, discount_amount, discount_label).print_receipt()


if __name__ == "__main__":
    FastBiteDiner().run()
"""Fast Bite Diner - Python OOP version. Run this file."""

from config import MENU
from input_helper import InputHelper
from menu import Menu
from order import Order
from receipt import Receipt


class FastBiteDiner:
    def __init__(self):
        self.menu = Menu(MENU)

    def take_orders(self):
        order = Order()
        while True:
            item_name = self.menu.ask_for_item()
            quantity = InputHelper.get_valid_quantity()
            order.add_item(item_name, self.menu.get_price(item_name), quantity)
            if not InputHelper.ask_yes_no("Order another item?"):
                break
        return order

    def run(self):
        self.menu.display()

        if not InputHelper.ask_yes_no("Would you like to place an order?"):
            print("Thank you for visiting Fast Bite Diner. Goodbye!")
            return

        order = self.take_orders()
        is_senior_or_pwd = InputHelper.ask_yes_no("Are you a Senior Citizen or PWD?")
        discount_amount, discount_label = order.get_discount(is_senior_or_pwd)
        Receipt(order, discount_amount, discount_label).print_receipt()


if __name__ == "__main__":
    FastBiteDiner().run()
