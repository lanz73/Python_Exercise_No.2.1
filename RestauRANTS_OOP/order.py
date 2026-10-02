"""OrderItem and Order classes."""


class OrderItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_line_total(self):
        return self.price * self.quantity


class Order:
    SENIOR_PWD_RATE = 0.20
    BULK_RATE = 0.10
    BULK_MIN_ITEMS = 5

    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        self.items.append(OrderItem(name, price, quantity))

    def get_subtotal(self):
        subtotal = 0.0
        for order_item in self.items:
            subtotal += order_item.get_line_total()
        return subtotal

    def get_total_quantity(self):
        total_items = 0
        for order_item in self.items:
            total_items += order_item.quantity
        return total_items

    def get_discount(self, is_senior_or_pwd):
        """Return (discount_amount, discount_label)."""
        subtotal = self.get_subtotal()
        if is_senior_or_pwd:
            return subtotal * self.SENIOR_PWD_RATE, "Senior Citizen/PWD Discount (20%)"
        elif self.get_total_quantity() >= self.BULK_MIN_ITEMS:
            return subtotal * self.BULK_RATE, "Bulk Order Promo (10%, 5+ items)"
        else:
            return 0.0, None
