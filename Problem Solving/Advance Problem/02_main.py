products_list = []

#---Product Add Functionalities
def add_product():
    p_id = input('Enter Product ID: ')
    p_name = input('Enter Product Name: ')
    p_price = int(input('Enter Product Price: '))
    p_qty = int(input("Enter Product Qty: "))

    p_data = {
        'p_id': p_id,
        'p_name': p_name,
        'p_price': p_price,
        'p_qty': p_qty,
        'total_price': p_price * p_qty
    }
    products_list.append(p_data)
    print('Product Successfully Added.')

#---Product view Functionalities
def view_product():
    for product in products_list:
        print(product)

#---Product search Functionalities
def search_product():
    product_id = input("Enter Product Id: ")
    for product in products_list:
        if product['p_id'] == product_id:
            print(product)
        else:
            print("Product Not Found")

#---Total Inventory calculate Functionalities
def total_inventory():
    total = 0
    count = 0
    for product in products_list:
        total += product['total_price']
        count +=1
    print(f'Total Inventory Value: {total}, Count: {count}')

#---Product delete Functionalities
def delete_product():
    product_id = input("Enter Product Id: ")
    if len(products_list) == 0:
        print("Product Not Available.")

    for product in products_list:
        if product['p_id'] == product_id:
            products_list.remove(product)
            print("Product Deleted Successfully")
        else:
            print("Product Not Found")

while True:
    print(f'Inventory System: ')
    print(f'''
    1. Add Product
    2. View Products
    3. Search Product
    4. Total Inventory Value
    5. Delete Product
    6. Exit
    ''')
    option = input("Enter your choice: ")
    if option == '1':
        add_product()
    elif option == '2':
        view_product()
    elif option == '3':
        search_product()
    elif option == '4':
        total_inventory()
    elif option == '5':
        delete_product()
    elif option == '6':
        break
    else:
        print("Enter Valid Input (1 to 6)")