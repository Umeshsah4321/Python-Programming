products = ["Rice", "Milk", "Bread"]

print("Original products:", products)

for i in range(3):
    product = input("Enter a new product: ")
    products.append(product)

print("Updated shopping list:", products)
print("Total number of products:", len(products))