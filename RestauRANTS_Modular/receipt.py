"""Receipt printing."""

from config import SEPARATOR


def print_receipt(orders, subtotal, discount_amount, discount_label):
    print("\n" + SEPARATOR)
    print("           FAST BITE DINER")
    print("         123 Mango Ave, Cebu City")
    print(SEPARATOR)
    print(f"{'ITEM':<18}{'QTY':>4}{'PRICE':>9}{'TOTAL':>9}")
    print("-" * 40)

    for order in orders:
        print(f"{order['item']:<18}{order['quantity']:>4}"
              f"{order['price']:>9.2f}{order['line_total']:>9.2f}")

    print("-" * 40)
    print(f"{'Subtotal':<31}Php {subtotal:>6.2f}")

    if discount_amount > 0:
        print(f"{discount_label:<31}-Php {discount_amount:>5.2f}")

    total = subtotal - discount_amount
    print("-" * 40)
    print(f"{'TOTAL DUE':<31}Php {total:>6.2f}")
    print(SEPARATOR)
    print("        Thank you for ordering!")
    print(SEPARATOR)
