

products = {}

data = input()
while data != "statistics":
    key, value = data.split(": ")
    value = int(value)
    if key not in products:
        products[key] = value
    else:
        products[key] += value
    data = input()
print(f"Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")