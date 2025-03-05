from collections import Counter

def checkout(skus: str) -> int:
    # Define item prices
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40
    }

    # Define special offers
    offers = {
        "A": [(5, 200), (3, 130)],  # 5A for 200, 3A for 130
        "B": [(2, 45)],  # 2B for 45
    }

    # Define "buy X get Y free" offers
    free_offers = {
        "E": (2, "B")  # Buy 2E, get 1B free
    }

    # Validate input (return -1 for invalid characters)
    for char in skus:
        if char not in prices:
            return -1

    # Count occurrences of each SKU
    item_counts = Counter(skus)

    # Apply "buy X get Y free" offers (e.g., 2E -> 1B free)
    for item, (req_qty, free_item) in free_offers.items():
        if item in item_counts and free_item in item_counts:
            free_items_count = item_counts[item] // req_qty
            item_counts[free_item] = max(0, item_counts[free_item] - free_items_count)

    # Calculate total price
    total = 0
    for item, count in item_counts.items():
        if item in offers:
            for offer_qty, offer_price in sorted(offers[item], reverse=True):  # Apply best offer first
                total += (count // offer_qty) * offer_price  # Apply offer
                count %= offer_qty  # Remaining items
        total += count * prices[item]  # Regular price for remaining items

    return total
