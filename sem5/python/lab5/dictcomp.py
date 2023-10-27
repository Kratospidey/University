item_prices = {
    "milk": 1.50,
    "bread": 2.25,
    "eggs": 0.98,
    "cheese": 3.75,
    "apple": 0.60,
    "orange": 0.75,
    "coffee": 4.50,
    "tea": 2.80,
    "chocolate": 2.50,
    "cereal": 3.85,
}


print()
print(f"Original Prices: \n{item_prices.items()}")

print()
print("Converted Prices:")

print(
    {item: round(price * 0.79, 2) for item, price in item_prices.items()}
)  # conversion rate is 0.79 on 30-08-23
