fruits=["apple", "banana", "cherry"]
vegetables=["carrot", "cabbage", "spinach"]
beverages=["water", "juice", "soda"]

fruits.append("orange")
vegetables.insert(1, "broccoli")
beverages.pop()

inventory=[fruits, vegetables, beverages]
print("Complete Inventory:", inventory)

print("First 2 fruits:", fruits[:2])

print("Last vegetable:", vegetables[-1])

fruit_lengths = [len(item) for item in fruits]
print("Lengths of fruit names:", fruit_lengths)

if("water"in beverages):
    print("Beverage available")
else:
    print("Beverage not available")  

tuples=(fruits[0], vegetables[0], beverages[0])
print("Tuple of first items from each section:",tuples)