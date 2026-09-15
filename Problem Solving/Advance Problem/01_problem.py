# Question: Inventory Management Application
# Example Run:
# INVENTORY MANAGEMENT
# ==============================
# 1. Add Product
# 2. View Products
# 3. Search Product
# 4. Inventory Value
# 5. Delete Product
# 6. Exit

product_list = []
def add_product():
    p_id= input("Enter Product Id:")
    p_name=input("Enter Product Name:")
    p_price=int(input("Enter Price:"))
    p_quantity=int(input("Enter Quantity:"))
    p_data={
        "p_id": p_id,
        "p_name": p_name,
        "p_price": p_price,
        "p_quantity":p_quantity,
        'total_price': p_price * p_quantity
    }
    product_list.append(p_data)
    print("Product Successfully Added")
    
def view_product():
    for product in product_list:
        for key, value in product.items():
            print(key,":", value)

def search_product():
    product_id= input("Enter Product Id: ")
    for product in product_list:
        if product['p_id']==product_id:
            print(product)
        else:
            print("Product Not Found")

def total_inventory():
    total=0
    count=0
    for product in product_list:
        total += product["total_price"]
        count += 1
    print(f"Total inventory:{total}, Count:{count}")

def del_product():
    product_id = input("Enter Product Id: ")

    for product in product_list:
        if product["p_id"] == product_id:
            product_list.remove(product)
            print("Delete Successfully")
        else:
            print("Product Not Found")

while True:
    print(f"Inventory System:")
    print(f"""
1. Add Product
2. View Products
3. Search Product
4. Inventory Value
5. Delete Product
6. Exit
""")
    option=input("Enter your choice: ")   
    if option == "1":
        add_product()
    elif option == "2":
        view_product()
    elif option == "3":
        search_product()
    elif option == "4":
        total_inventory()
    elif option == "5":
        del_product()
    elif option == "6":
        print("Thank you")
        break
    else:
        print("Enter Valid Input (1 to 6) ")
