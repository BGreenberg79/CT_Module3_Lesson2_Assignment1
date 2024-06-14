# Task 1 Custom Order Processing

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

def unpack_tup_print(order_list):
    for index, tup in enumerate(order_list,1):
        customer_name, product, quantity = tup
        print(f"\nOrder #{str(index)}\nCustomer Name: {customer_name.title()} \nProduct Name: {product.title()} \nQuantity: {str(quantity)}")

unpack_tup_print(orders)

'''
Our function works by numbering our list of orders through the built in enumerate function and further works by unpacking the second tup variable in the enumerate fucntion that houses each tuple so
we can access each individual piece of data as we build the print statement that we are looping through.
Crucially to avoid any TypeError or ValueErrors I am sure to convert both the index from our enumerate function and the quantity from the tuple contents from integer to string within our f-string so python can cleanly print our numeric results as well. 
Lastly, after this simple function is built I run it with the list of orders that the assignment gave us.
'''