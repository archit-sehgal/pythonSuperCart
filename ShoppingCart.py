categories = {
    "Laptop": [{
        "Dell": {"Id": 101, "Name": "dell_inspiron", "Price": 55000},
        "Asus": {"Id": 201, "Name": "asus_tuf", "Price": 65000},
        "Mac": {"Id": 301, "Name": "macbook_pro", "Price": 95000}
    }],
    "SmartPhone": [{
        "Iphone": {"Id": 401, "Name": "iphone_11", "Price": 30000},
        "OnePlus": {"Id": 501, "Name": "oneplus_nord", "Price": 25000},
        "Nothing": {"Id": 601, "Name": "nothing_2", "Price": 35000}
    }],
    "Accessories": [{
        "Cable": {"Id": 701, "Name": "cable", "Price": 1000},
        "Cover": {"Id": 801, "Name": "cover", "Price": 500},
        "Adapter": {"Id": 901, "Name": "adapter", "Price": 2000}
    }]
}

def findName(AllProducts):
    for i in categoriesName:
        for x in categories[i][0].values():
            AllProducts.append(x["Name"])

def findSelectedProducts(customerSelectedItem, ProductsSelected, quantityselected):
    for i in categoriesName:
        for x in categories[i][0].values():
            if x["Name"] == customerSelectedItem:
                ProductsSelected.append(
                    {"Name": x["Name"], "Price": x["Price"], "Qty": quantityselected}
                )

def findPrice(ProductsSelected, quantityselected):
    TotalAmount = 0
    for p in ProductsSelected:
        TotalAmount += p["Price"] * quantityselected
    return TotalAmount

def showAllProducts():
    for i in categories:
        print(i + " Products:")
        for p in categories[i][0]:
            print("  ~", categories[i][0][p]["Name"]," -",categories[i][0][p]["Price"])

AllProducts = []
categoriesName = ["Laptop", "SmartPhone", "Accessories"]
findName(AllProducts)
ProductsSelected = []

isShopping = True
while isShopping:
    showAllProducts()
    customerSelectedItem = input("Enter the product name you want: ")
    quantityselected = int(input("Enter quantity: "))
    findSelectedProducts(customerSelectedItem, ProductsSelected, quantityselected)
    wantToAddMoreItems = input("Do you want to add more products? (y/n): ")
    if wantToAddMoreItems.lower() != "y":
        isShopping = False

Total = findPrice(ProductsSelected, quantityselected)
print("-----------------")
print("Selected Products:")
print("-----------------")
for product in ProductsSelected:
    print(product["Name"], "- Qty:", product["Qty"], "- Price:" + str(product["Price"]))
    print("------------------------------------")

print("Your cart total is:","\n--------","\n" ,Total,"\n--------")
