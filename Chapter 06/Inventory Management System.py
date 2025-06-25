# Initialize the inventory dictionary 
inventory = {} 
# Function to add a product 
def add_product(product_id, name, quantity, price): 
    inventory[product_id] = {'name': name, 'quantity': quantity, 'price': price} 
# Function to update a product 
def update_product(product_id, name=None, quantity=None, price=None): 
    if product_id in inventory: 
        if name: 
            inventory[product_id]['name'] = name 
        if quantity: 
            inventory[product_id]['quantity'] = quantity 
        if price: 
            inventory[product_id]['price'] = price 
        else: print("Product not found.") 
# Function to remove a product 
def remove_product(product_id): 
    if product_id in inventory: 
        del inventory[product_id] 
    else: print("Product not found.") 
# Function to view all products 
def view_inventory(): 
    for product_id, details in inventory.items(): 
        print(f"ID: {product_id}, Details: {details}") 

# Adding products 
add_product(1, "Tea", 100, 1.99) 
add_product(2, "Coffee", 50, 2.99) 
# Updating a product 
update_product(1, quantity=150) 
# Viewing inventory 
view_inventory() 
# Removing a product 
remove_product(2) 
# Viewing inventory after removal 
view_inventory()
