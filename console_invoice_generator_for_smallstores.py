import json
from datetime import datetime

# 1. Product class
class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, qty):
        self.stock += qty

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price, "stock": self.stock}

    @classmethod
    def from_dict(cls, d):
        return cls(d['id'], d['name'], d['price'], d['stock'])

# 2. InvoiceItem class
class InvoiceItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total_price = round(product.price * quantity, 2)

# 3. Invoice class
class Invoice:
    TAX_RATE = 0.07  # 7% tax, adjust as needed

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
        self.subtotal = 0
        self.tax = 0
        self.total = 0
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def add_item(self, inv_item):
        self.items.append(inv_item)
        self.calculate_total()

    def calculate_total(self):
        self.subtotal = sum(item.total_price for item in self.items)
        self.tax = round(self.subtotal * Invoice.TAX_RATE, 2)
        self.total = round(self.subtotal + self.tax, 2)

    def print_invoice(self):
        separator = "="*40
        print(separator)
        print(f"INVOICE   Date: {self.date}")
        print(f"Customer: {self.customer_name}")
        print(separator)
        print(f"{'ID':<5} {'Product':<18} {'Qty':<5} {'Price':<8}")
        print("-"*40)
        for item in self.items:
            print(f"{item.product.id:<5} {item.product.name:<18} {item.quantity:<5} {item.total_price:<8.2f}")
        print("-"*40)
        print(f"{'Subtotal':<28}: {self.subtotal:.2f}")
        print(f"{'Tax (7%)':<28}: {self.tax:.2f}")
        print(f"{'Total':<28}: {self.total:.2f}")
        print(separator)

    def save_invoice(self):
        fname = f"Invoice_{self.customer_name}_{self.date.replace(':', '-')}.txt"
        with open(fname, "w") as f:
            f.write(f"INVOICE   Date: {self.date}\n")
            f.write(f"Customer: {self.customer_name}\n")
            f.write("="*40 + "\n")
            f.write(f"{'ID':<5} {'Product':<18} {'Qty':<5} {'Price':<8}\n")
            for item in self.items:
                f.write(f"{item.product.id:<5} {item.product.name:<18} {item.quantity:<5} {item.total_price:<8.2f}\n")
            f.write("-"*40 + "\n")
            f.write(f"{'Subtotal':<28}: {self.subtotal:.2f}\n")
            f.write(f"{'Tax (7%)':<28}: {self.tax:.2f}\n")
            f.write(f"{'Total':<28}: {self.total:.2f}\n")
            f.write("="*40 + "\n")
        print(f"Saved invoice to {fname}")

# 4. InventoryManager class
class InventoryManager:
    def __init__(self, filename="products.json"):
        self.filename = filename
        self.products = []
        self.load_products()

    def add_product(self, prod):
        self.products.append(prod)

    def update_product(self, prod_id, name=None, price=None, stock=None):
        for prod in self.products:
            if prod.id == prod_id:
                if name:
                    prod.name = name
                if price is not None:
                    prod.price = price
                if stock is not None:
                    prod.stock = stock
                break

    def load_products(self):
        try:
            with open(self.filename, "r") as f:
                plist = json.load(f)
                self.products = [Product.from_dict(d) for d in plist]
        except FileNotFoundError:
            self.products = []

    def save_products(self):
        with open(self.filename, "w") as f:
            json.dump([p.to_dict() for p in self.products], f, indent=2)

    def view_products(self):
        print("="*44)
        print(f"{'ID':<5} {'Name':<20} {'Price':<8} {'Stock':<5}")
        print("-"*44)
        for prod in self.products:
            print(f"{prod.id:<5} {prod.name:<20} {prod.price:<8.2f} {prod.stock:<5}")
        print("="*44)

    def find_product_by_id(self, prod_id):
        for prod in self.products:
            if prod.id == prod_id:
                return prod
        return None

# Main Function 

def main():
    inv_manager = InventoryManager()
    while True:
        print("\n1. Add Product  2. Update Product  3. View Products  4. Create Invoice  5. Save products to file  6. Load products from file  0. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            id = input("Product id: ")
            name = input("Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            prod = Product(id, name, price, stock)
            inv_manager.add_product(prod)
            print("Product added.")
        elif choice == '2':
            id = input("Product id to update: ")
            prod = inv_manager.find_product_by_id(id)
            if prod:
                name = input(f"New name ({prod.name}): ") or prod.name
                price = input(f"New price ({prod.price}): ")
                price = float(price) if price else prod.price
                stock = input(f"New stock ({prod.stock}): ")
                stock = int(stock) if stock else prod.stock
                inv_manager.update_product(id, name, price, stock)
                print("Product updated.")
            else:
                print("Product not found.")
        elif choice == '3':
            inv_manager.view_products()
        elif choice == '4':
            customer = input("Customer name: ")
            invoice = Invoice(customer)
            inv_manager.view_products()
            while True:
                prod_id = input("Enter product ID to add (blank to finish): ")
                if not prod_id:
                    break
                prod = inv_manager.find_product_by_id(prod_id)
                if prod and prod.stock > 0:
                    qty = int(input(f"Enter quantity for {prod.name}: "))
                    if 0 < qty <= prod.stock:
                        item = InvoiceItem(prod, qty)
                        invoice.add_item(item)
                        prod.update_stock(-qty)
                        print("Added to invoice.")
                    else:
                        print("Invalid quantity.")
                else:
                    print("Product not found or out of stock.")
            invoice.print_invoice()
            invoice.save_invoice()
            inv_manager.save_products()
        elif choice == '5':
            inv_manager.save_products()
            print("Products saved to file.")
        elif choice == '6':
            inv_manager.load_products()
            print("Products loaded from file.")
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()  # Run the application


# Utility: To clear file after session, use:
# from os import remove; remove("products.json") if you wish
