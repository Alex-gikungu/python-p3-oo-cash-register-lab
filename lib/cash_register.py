#!/usr/bin/env python3

class CashRegister:
    def __init__(self):
        self.items = []
        self.prices = []
        self.quantities = []
        self.discount = 0
        self.last_transaction = 0

    def add_item(self, item_name, price, quantity=1):
        self.items.append(item_name)
        self.prices.append(price)
        self.quantities.append(quantity)
        self.last_transaction = price * quantity

    def calculate_discount(self, discount_percentage):
        self.discount = discount_percentage

    def void_last_transaction(self):
        self.items.pop()
        self.prices.pop()
        self.quantities.pop()
        self.last_transaction = 0

    def get_total(self):
        total = sum([price * quantity for price, quantity in zip(self.prices, self.quantities)])
        total -= total * self.discount / 100
        return total

if __name__ == "__main__":
    register = CashRegister()
    register.add_item("Item 1", 10, 2)
    register.add_item("Item 2", 20, 1)
    register.calculate_discount(10)
    print("Total before void:", register.get_total()) 
    register.void_last_transaction()
    print("Total after void:", register.get_total())  

