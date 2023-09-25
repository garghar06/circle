class ShoppingCart:
    def __init__(self):
        self.items = {}  

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if quantity >= self.items[item_name]['quantity']:
                del self.items[item_name]
            else:
                self.items[item_name]['quantity'] -= quantity

    def calculate_total(self):
        total = 0
        for item_name, item_info in self.items.items():
            total += item_info['price'] * item_info['quantity']
        return total

 
    def view_cart(self):
        for item_name, item_info in self.items.items():
            print(f"{item_name}: {item_info['quantity']} x ${item_info['price']} each")


cart = ShoppingCart()

cart.add_item("Apples", 100)
cart.add_item("Wheat flour", 140, 3)
cart.add_item("Cucumber", 40,4)

cart.view_cart()

print("Total Price:", cart.calculate_total())

cart.remove_item("Cucumber")

cart.view_cart()