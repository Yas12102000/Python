# Product Class
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
    

# Inventory Class
class Inventory:
    def __init__(self):
        self.products = []
    
    # Add Method
    def add_product(self, product):
        self.products.append(product)

    # Remove Method
    def remove_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print(f"Product {product_id} removed.")
                return
            
        print(f"Product {product_id} not found.")

    # Update Method
    def update_quantity(self, product_id, new_quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity == new_quantity
                print(f"Quantity updated for product {product_id}.")
                return
        
        print(f"Product {product_id} not found.")

    # Search Method
    def search_product(self, search_term):
        results = []
        for product in self.products:
            if search_term.lower() in product.name.lower() or search_term == str(product.product_id):
                results.append(product)

        return results
    
    # Display Method
    def display_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            for product in self.products:
                print(product)

    # Save Method
    def save_inventory(self, filename):
        with open(filename, 'w') as file:
            for product in self.products:
                file.write(f"{product.product_id}, {product.name}, {product.price}, {product.quantity}\n")
        print(f"Inventory saved to {filename}.")

    # Load Method
    def load_inventory(self, filename):
        self.products = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    product_id, name, price, quantity = line.strip().split(',')
                    self.products.append(Product(int(product_id), name, float(price), int(quantity)))
            print(f"Inventory loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not fount.")


# Menu For User Interaction
def display_menu():
    print("\nRetail Inventory Management System")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Update Product Quantity")
    print("4. Search Product")
    print("5. Display Inventory")
    print("6. Save Inventory")
    print("7. Load Inventory")
    print("8. Exit")

def main():
    inventory = Inventory()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(product_id, name, price, quantity)
            inventory.add_product(product)
            print("Product added.")

        elif choice == '2':
            product_id = int(input("Enter product ID to remove: "))
            inventory.remove_product(product_id)

        elif choice == '3':
            product_id = int(input("Enter product ID to update: "))
            new_quantity = int(input("Enter new quantity: "))
            inventory.update_quantity(product_id, new_quantity)

        elif choice == '4':
            search_term = input("Enter product name or ID to search: ")
            results = inventory.search_product(search_term)
            if results:
                print("Search results:")
                for product in results:
                    print(product)
            else:
                print("No matching products found.")

        elif choice == '5':
            inventory.display_inventory()

        elif choice == '6':
            filename = input("Enter filename to save inventory: ")
            inventory.save_inventory(filename)

        elif choice == '7':
            filename = input("Enter filename to load inventory: ")
            inventory.load_inventory(filename)

        elif choice == '8':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()