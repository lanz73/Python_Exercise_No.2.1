"""Receipt class: prints the final receipt for an order."""

from config import SEPARATOR


class Receipt:
    def __init__(self, order, discount_amount, discount_label):
        self.order = order
        self.discount_amount = discount_amount
        self.discount_label = discount_label

    def print_receipt(self):
        subtotal = self.order.get_subtotal()

        print("\n" + SEPARATOR)
        print("           FAST BITE DINER")
        print("         123 Mango Ave, Cebu City")
        print(SEPARATOR)
        print(f"{'ITEM':<18}{'QTY':>4}{'PRICE':>9}{'TOTAL':>9}")
        print("-" * 40)

        for order_item in self.order.items:
            print(f"{order_item.name:<18}{order_item.quantity:>4}"
                  f"{order_item.price:>9.2f}{order_item.get_line_total():>9.2f}")

        print("-" * 40)
        print(f"{'Subtotal':<31}Php {subtotal:>6.2f}")

        if self.discount_amount > 0:
            print(f"{self.discount_label:<31}-Php {self.discount_amount:>5.2f}")

        total = subtotal - self.discount_amount
        print("-" * 40)
        print(f"{'TOTAL DUE':<31}Php {total:>6.2f}")
        print(SEPARATOR)
        print("        Thank you for ordering!")
        print(SEPARATOR)
