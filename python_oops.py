class ShoppingCart:
    products = {'iphone': 5, 'imac': 3, 'ipad': 2, 'iwatch': 1}

    prices = {'iphone': 900, 'imac': 5000, 'ipad': 3000, 'iwatch': 4000}

    def __init__(self):
        self.cart = []

    def add_items(self, name, quantity):
        try:
            if name not in ShoppingCart.products:
                raise KeyError("Product not available")

            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero")

            if quantity > ShoppingCart.products[name]:
                raise ValueError("Product out of stock")

            item = {'name': name, 'quantity': quantity,
                    'price': ShoppingCart.prices[name]}

            self.cart.append(item)
            ShoppingCart.products[name] -= quantity

            print(f"{quantity} {name}(s) added to cart")

        except KeyError as e:
            print("Error:", e)

        except ValueError as e:
            print("Error:", e)

        except Exception as e:
            print("Unexpected error:", e)

    def remove_item(self, name):
        try:
            for item in self.cart:
                if item['name'] == name:
                    if item['quantity'] > 1:
                        item['quantity'] -= 1
                        ShoppingCart.products[name] += 1
                    else:
                        self.cart.remove(item)
                        ShoppingCart.products[name] += 1
                    print(f"{name} removed from cart")
                    return

            raise KeyError("Item not found in cart")

        except KeyError as e:
            print("Error:", e)

    def total_price(self):
        try:
            if not self.cart:
                raise ValueError("Cart is empty")

            total = 0
            for item in self.cart:
                total += item['quantity'] * item['price']

            return total

        except ValueError as e:
            print("Error:", e)
            return 0

        
c1 = ShoppingCart()

c1.add_items('iphone', 6)   # out of stock
c1.add_items('iphone', 2)
c1.add_items('IPhone', 1)   # wrong case

print(c1.total_price())
