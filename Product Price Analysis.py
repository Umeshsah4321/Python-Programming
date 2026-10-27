products = {
    "Laptop": 80000,
    "Mobile": 30000,
    "Keyboard": 2000,
    "Mouse": 1000,
    "Monitor": 25000
}

print("Product Details")

for name, price in products.items():
    print(name, ":", price)

total_price = sum(products.values())

most_expensive = max(products, key=products.get)

print("Total price:", total_price)
print("Most expensive product:", most_expensive)
print("Highest price:", products[most_expensive])