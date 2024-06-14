# Task 1 Product Catalogue Merging

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

def join_catalogs(*catalogs):
    joined_catalogs = ()
    for catalog in catalogs:
        joined_catalogs += catalog
    return joined_catalogs

'''
I use the *args feature to be able to take in any future additional catalogs that ay be added to the program beyond the first two.
I then initialize the joined catalogs tuple and loop through the argument of *catalogs adding joining each catalog to the joined_catalogs tuple I initiated.
I then exit the for loop and return joined_catalogs
'''
joined_catalogs_test_1 = join_catalogs(catalog1, catalog2)
print(joined_catalogs_test_1)
#Test case to show that join_catalogs(*catalogs) is working, terminal shows inner tuples of (product, price) pair have been preserved and order has gone unchanged since joining catalogs.
catalog3 = (("Sneakers", 300), ("Backpack", 60))
joined_catalogs_test_2 = join_catalogs(catalog1, catalog2, catalog3)
print(joined_catalogs_test_2)
#Function still works after adding a third catalog tuple
joined_catalogs_test_3 = join_catalogs(catalog3)
print(joined_catalogs_test_3)
#Function works even when passing through only one catalog

def display_catalogs (joined_catalog_result):
    print("Items from the joined catalog in the order each catalog was added and in the order they were found in their original catalog:\n")
    for index, catalog in enumerate(joined_catalog_result,1):
        print(f"Product {str(index)}: {catalog[0]}\tPrice: {catalog[1]}")
print("\n")
display_catalogs(joined_catalogs_test_2)

'''
I used the ealier tests to demonstate that our join function worked the way we anticipated keeping an our tuple for the entire collection of products and inner tuples for each individual product and its price, but excluding the tuple for each individual catalog.
For my second display_catalogs function I used the enumerate function and a for loop to create a user friendly view of the entire joiend catalog numbering each product in the order they were added (while also maintaining their original order inside their original catalog)
and also listing the name and product using the index locations of the inner tuples.
'''