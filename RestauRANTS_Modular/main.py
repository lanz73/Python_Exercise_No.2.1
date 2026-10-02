"""Fast Bite Diner - Modular version. Run this file."""

from config import MENU
from menu import display_menu
from input_helpers import ask_yes_no
from orders import take_orders, calculate_subtotal, get_discount
from receipt import print_receipt


def main():
    display_menu(MENU)

    if not ask_yes_no("Would you like to place an order?"):
        print("Thank you for visiting Fast Bite Diner. Goodbye!")
        return

    orders = take_orders(MENU)
    subtotal = calculate_subtotal(orders)
    discount_amount, discount_label = get_discount(orders, subtotal)
    print_receipt(orders, subtotal, discount_amount, discount_label)


if __name__ == "__main__":
    main()
