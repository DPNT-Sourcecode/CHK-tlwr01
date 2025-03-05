from collections import Counter

def checkout(skus: str) -> int:
    # Price table for all items
    prices = {
        "A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10,
        "G": 20, "H": 10, "I": 35, "J": 60, "K": 80, "L": 90,
        "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50,
        "S": 30, "T": 20, "U": 40, "V": 50, "W": 20, "X": 90,
        "Y": 10, "Z": 50
    }

    # Multi-buy special offers (list of tuples: (quantity, special price))
    # Sorted later by quantity in descending order for optimal application.
    offers = {
        "A": [(5, 200), (3, 130)],
        "B": [(2, 45)],
        "H": [(10, 80), (5, 45)],
        "K": [(2, 150)],
        "P": [(5, 200)],
        "Q": [(3, 80)],
        "V": [(3, 130), (2, 90)]
    }

    # "Buy X get Y free" offers:
    # Format: trigger_item: (required_qty, free_item, free_count)
    free_offers = {
        "E": (2, "B", 1),   # For every 2 E, one B is free.
        "N": (3, "M", 1),   # For every 3 N, one M is free.
        "R": (3, "Q", 1),   # For every 3 R, one Q is free.
        "U": (3, "U", 1),   # For every 3 U, one U is free (i.e. pay for 2 out of 3).
        "F": (3, "F", 1)    # For every 3 F, one F is free (i.e. pay for 2).
    }

    # Validate input: if any SKU is not in prices, return -1.
    for ch in skus:
        if ch not in prices:
            return -1

    # Count the occurrences of each SKU
    counts = Counter(skus)

    # Apply free offers first.
    # For each free-offer, determine how many free items should be removed.
    for trigger, (req_qty, free_item, free_count) in free_offers.items():
        if trigger in counts:
            num_triggers = counts[trigger]
            # Calculate number of free items earned
            free_items_earned = (num_triggers // req_qty) * free_count
            # Deduct free items from free_item count, ensuring it does not go below 0.
            if free_item in counts:
                counts[free_item] = max(0, counts[free_item] - free_items_earned)
            else:
                counts[free_item] = 0

    total = 0
    # Process each item in the basket.
    for item, count in counts.items():
        # If there are multi-buy offers for the item, apply them in order of best offer (largest quantity first).
        if item in offers:
            # Sort the offers in descending order of quantity.
            for offer_qty, offer_price in sorted(offers[item], key=lambda x: x[0], reverse=True):
                if count >= offer_qty:
                    num_offers = count // offer_qty
                    total += num_offers * offer_price
                    count %= offer_qty
        # Add the cost of any remaining items at regular price.
        total += count * prices[item]

    return total
