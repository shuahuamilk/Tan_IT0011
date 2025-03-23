class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: {self.price:.2f}"


class ItemManager:
    def __init__(self):
        self.items = {}
    #item creation
    def create_item(self):
        try:
            item_id = int(input("Enter item ID: "))
            if item_id in self.items:
                print("Error: Item ID already exists.")
                return
            name = input("Enter item name: ").strip()
            description = input("Enter item description: ").strip()
            price = float(input("Enter item price: "))
            if price < 0:
                print("Error: Price cannot be negative.")
                return
            
            self.items[item_id] = Item(item_id, name, description, price)
            print("Item added successfully!")
        except ValueError:
            print("Error: Invalid input. Please enter valid values.")
    #view items
    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)
    #update item
    def update_item(self):
        try:
            item_id = int(input("Enter item ID to update: "))
            if item_id not in self.items:
                print("Error: Item not found.")
                return
            
            name = input("Enter new name: ").strip()
            description = input("Enter new description: ").strip()
            price = float(input("Enter new price: "))
            if price < 0:
                print("Error: Price cannot be negative.")
                return
            
            self.items[item_id] = Item(item_id, name, description, price)
            print("Item updated successfully!")
        except ValueError:
            print("Error: Invalid input. Please enter valid values.")
    #delete item
    def delete_item(self):
        try:
            item_id = int(input("Enter item ID to delete: "))
            if item_id in self.items:
                del self.items[item_id]
                print("Item deleted successfully!")
            else:
                print("Error: Item not found.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid item ID.")

#main menu
def main():
    manager = ItemManager()
    
    while True:
        print("\nItem Management System")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            manager.create_item()
        elif choice == '2':
            manager.read_items()
        elif choice == '3':
            manager.update_item()
        elif choice == '4':
            manager.delete_item()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

#program execution
if __name__ == "__main__":
    main()
