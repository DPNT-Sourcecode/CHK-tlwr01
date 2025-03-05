from collections import Counter

def checkout(skus: str) -> int:
    # Define item prices
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15
    }

    # Define special offers
    offers = {
        "A": (3, 130),  # 3A for 130
        "B": (2, 45)    # 2B for 45
    }

    # Validate input (return -1 for invalid characters)
    for char in skus:
        if char not in prices:
            return -1

    # Count occurrences of each SKU
    item_counts = Counter(skus)

    # Calculate total price
    total = 0
    for item, count in item_counts.items():
        if item in offers:
            offer_qty, offer_price = offers[item]
            total += (count // offer_qty) * offer_price  # Apply offer price
            total += (count % offer_qty) * prices[item]  # Add remaining items
        else:
            total += count * prices[item]  # Regular price for non-offer items

    return total


