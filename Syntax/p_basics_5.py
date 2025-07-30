# OOP 

# # Classes & object

# # car data 

# car = {
#     "name": "janisar"
# }

# # class
# class Car:
#     def __init__(self, brand, model, is_New, ownerShip):
#         self.brand = brand
#         self.model = model
#         self.is_New = is_New
#         self.ownerShip = ownerShip
#     # def __str__(self):
#     #     return f"{self.is_New}"
#     def salmanCar(self):
#         return f"Salman purchased this {self.brand} car!"


# # object
# car1 = Car("mehran",2019,False,3)
# print("Car 1: ",car1.salmanCar())



# Task 01

# Class to represent a single grocery item
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Class to represent the Grocery Store
class GroceryStore:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print("\n Store Inventory:")
        for item in self.inventory:
            print(f"- {item.name}: Rs. {item.price}")

# Class to represent the customer's shopping cart
class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, item):
        self.cart_items.append(item)

    def generate_bill(self):
        print("\n Final Bill:")
        total = 0
        for item in self.cart_items:
            print(f"{item.name}: Rs. {item.price}")
            total += item.price
        print(f"Total Amount: Rs. {total}")

# ------------------ USE CASE ------------------

# Create store
store = GroceryStore()

# Add items to inventory
store.add_item(Item("Milk", 150))
store.add_item(Item("Bread", 80))
store.add_item(Item("Eggs", 200))
store.add_item(Item("Sugar", 90))

# Display items
store.show_inventory()

# Create customer's cart
cart = ShoppingCart()

# Simulate user adding items to cart
cart.add_to_cart(Item("Milk", 150))
cart.add_to_cart(Item("Bread", 80))
cart.add_to_cart(Item("Sugar", 90))

# Generate the bill
cart.generate_bill()
