# # OOP 

# # # Classes & object

# # # car data 

# # car = {
# #     "name": "janisar"
# # }

# # # class
# # class Car:
# #     def __init__(self, brand, model, is_New, ownerShip):
# #         self.brand = brand
# #         self.model = model
# #         self.is_New = is_New
# #         self.ownerShip = ownerShip
# #     # def __str__(self):
# #     #     return f"{self.is_New}"
# #     def salmanCar(self):
# #         return f"Salman purchased this {self.brand} car!"


# # # object
# # car1 = Car("mehran",2019,False,3)
# # print("Car 1: ",car1.salmanCar())



# # Task 01

# # Class to represent a single grocery item
# class Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity


# # Class to represent the Grocery Store
# class GroceryStore:
#     def __init__(self):
#         self.inventory = []

#     def add_item(self, item):
#         self.inventory.append(item)

#     def show_inventory(self):
#         print("\n Store Inventory:")
#         for item in self.inventory:
#             print(f"- {item.name}: Rs. {item.price} Quantity: {item.quantity}")

# # Class to represent the customer's shopping cart
# class ShoppingCart:
#     def __init__(self):
#         self.cart_items = []

#     def add_to_cart(self, item):
#         self.cart_items.append(item)

#     def generate_bill(self):
#         print("\n Final Bill:")
#         total = 0
#         for item in self.cart_items:
#             print(f"{item.name}: Rs. {item.price}")
#             total += item.price
#         print(f"Total Amount: Rs {total}")


# # ------------------ USE CASE ------------------

# print("------------------ Imtiaz Super Market ------------------")
# # Create store
# store = GroceryStore()
# shopCart = ShoppingCart()

# option = input("Press 1 for Admin interface \n Press 2 for Customer Interface: ")
# if option == "1":
#     print("------------------ Welcome to Admin Interface ------------------")
#     option1 = input("1-Show Inventory \n 2- Add Item in Inventory: ")
#     if option1 == "1":
#         store.show_inventory()
#     elif option1 == "2":
#         itemName = input("Enter item name: ")
#         itemPrice = input("Enter item price: ")
#         itemQuantity = input("Enter item quantity: ")

#         store.add_item(Item(itemName, itemPrice, itemQuantity))
#     else:
#         print("Invalid Input!")
# elif option == "2":
#     print("------------------Welcome to Customer Interface------------------")

#     valueItem = input("Add to cart item: ")
#     inventory = store.inventory
#     for item in inventory:
#         if item == valueItem:
#            shopCart.add_to_cart(valueItem)
#         else:
#             print("Out of stock!")
# else:
#     print("Option is not correct!")

