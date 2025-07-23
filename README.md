# InvoicePro-Console_Invoice_Generator_for_Small_Stores
This "InvoicePro – Console Invoice Generator for Small Stores" project, covering the background, objectives, key features, design and workflow.

Project Overview
----------------

InvoicePro is a Python console application designed to help small storekeepers manage their inventory (products), create detailed invoices (bills) for customers, and keep digital records, all through simple terminal interactions. It is especially suited for environments where advanced graphical software isn’t available, making basic automation accessible for everyday store operations.

Objectives
----------

Inventory Management: Easily add, update, and view products.

Billing: Create professional invoices with tax calculations, clear product details, and accurate totals.

Record Keeping: Save product catalogs and invoices as files, enabling digital history and easy data recovery.

User-Friendly: Provide a simple, menu-driven console interface suitable for users with minimal technical background.

Key Features
------------

A. Product Management:

->Add new products (name, price, stock).

->Update existing product details.

->View all products currently in the catalog.

->Products stored in a JSON file (products.json) for easy loading and saving.

B. Invoice Creation:

->Enter a customer’s name.

->Add multiple product items to an invoice (choosing quantity and seeing subtotal).

->Automatically deduct purchased quantities from stock.

C. Invoice/Bill Generation:

->Calculates subtotal, tax, and total at checkout.

->Prints each invoice in a clear, formatted "receipt" style (showing date/time, customer name, itemized list, totals).

->Saves each invoice as a .txt file with a unique timestamped filename.

Class and Module Design
-----------------------

The project is organized using object-oriented programming (OOP). Each major part of the business logic is represented by a class. Here’s how each part works:

A. Product Class:

Represents a single store product.

Attributes:

->id (Product code)

->name (Product name)

->price (Unit price)

->stock (Available quantity)

Methods:

->update_stock(qty): Increase or decrease stock.

->to_dict(), from_dict(): Convert between Python objects and dictionaries (for file I/O).

B. InvoiceItem Class:

Represents a single item (product + quantity) on an invoice.

Attributes:

->product (Product object)

->quantity (Units being sold)

->total_price (product.price × quantity)

C. Invoice Class:

Handles one complete bill/invoice for a customer.

Attributes:

->customer_name

->items (List of InvoiceItems)

->subtotal (Sum before tax)

->tax, total

->date (Date/time of invoice creation)

Methods:

->add_item(): Attach an item to the invoice.

->calculate_total(): Automatically update subtotal, tax, total.

->print_invoice(): Print a structured, pretty receipt.

->save_invoice(): Write invoice to a .txt file.

D. InventoryManager Class:

Handles product collection, loading from/saving to file, and searching.

Attributes:

->filename (e.g., "products.json")

->products (List of Product objects)

Methods:

->add_product(), update_product(), view_products()

->load_products(), save_products()

->find_product_by_id(): Search product by ID.

How The Application Works (Workflow)
------------------------------------

Menu-Driven Console Interface:

The user interacts with a numbered menu:

text

1. Add Product  

2. Update Product  

3. View Products  

4. Create Invoice  

5. Save products to file  

6. Load products from file  

0. Exit

Detailed Flow:

->Add Product

->User inputs product details.

->Product is added to the in-memory list.

->Update Product

->User enters an existing product ID.

->Can change name, price, or stock for that product.

->View Products

->Product table is displayed, showing code, name, price, and stock.

->Create Invoice

->User enters customer name.

->Products are displayed for selection.

For each item:

->User picks product ID and quantity.

->Stock is checked, and reduced if valid.

->Items are added to the invoice.

On finishing:

->Structured invoice (receipt) is printed.

->Invoice is saved to a .txt file for records.

->Product records are automatically saved.

Save/Load Products

->Products are saved to or loaded from products.json.

Exit

Leaves the application.

File Handling
-------------

products.json
->Stores the entire catalog in JSON format. Lets you keep your product list between program runs.

Invoice text files
->Each invoice is saved in a timestamped .txt file. These can be printed, stored, retrieved, or shared as proof of sale.

Design Highlights And Benefits
------------------------------

->Uses OOP with clear separation of concerns (product logic, invoice logic, inventory logic).

->File I/O for persistent data. You won’t lose your product list or invoices.

->Simple, readable receipts, formatted much like real-world shop bills.

->User-friendly: Each menu is self-explanatory; input validation guides users.

->Easy to extend: Change tax rates, add more product details, integrate with databases, or add user authentication in future.

Typical Session Example
-----------------------

Start:

->Menu appears.

Add Product:

->Enter ID: 101

->Name: Soap

->Price: 20

->Stock: 50

View Products:

text

|  ID  |  Name  |  Price  |  Stock  |

|  101 |  Soap  |  20.00  |   50    |

Create Invoice:

->Customer: John

->Add item: ID 101, qty 2
(Stock reduced to 48)

->Finish.

->Receipt (with totals, tax, etc.) printed and saved.

Conclusion:
-----------

InvoicePro demonstrates practical software development for real-life needs in small business, using logical OOP structures, file-based persistence, and easy-to-use console interaction.

->System design and modularity

->Proper use of Python classes and methods

->Persistent storage through file operations

->Terminal-based user interface and interaction design
