"""Taking orders, computing the subtotal, and applying discounts."""

from config import SENIOR_PWD_RATE, BULK_RATE, BULK_MIN_ITEMS
from input_helpers import ask_yes_no, get_valid_menu_item, get_valid_quantity


def take_orders(menu):
    orders = []
    while True:
        item = get_valid_menu_item(menu)
        quantity = get_valid_quantity()
        orders.append({"item": item, "quantity": quantity, "price": menu[item]})
        if not ask_yes_no("Order another item?"):
            break
    return orders


def calculate_subtotal(orders):
    subtotal = 0.0
    for order in orders:
        line_total = order["price"] * order["quantity"]
        order["line_total"] = line_total
        subtotal += line_total
    return subtotal


def get_discount(orders, subtotal):
    total_items = 0
    for order in orders:
        total_items += order["quantity"]

    if ask_yes_no("Are you a Senior Citizen or PWD?"):
        return subtotal * SENIOR_PWD_RATE, "Senior Citizen/PWD Discount (20%)"
    elif total_items >= BULK_MIN_ITEMS:
        return subtotal * BULK_RATE, "Bulk Order Promo (10%, 5+ items)"
    else:
        return 0.0, None
