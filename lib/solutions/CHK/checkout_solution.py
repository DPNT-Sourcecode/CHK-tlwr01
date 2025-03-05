from collections import Counter

def checkout(skus: str) -> int:
    # Updated price table
    prices = {
        "A": 50, "B": 30, "C": 20, "D": 15,
        "E": 40, "F": 10, "G": 20, "H": 10,
        "I": 35, "J": 60, "K": 70, "L": 90,
        "M": 15, "N": 40, "O": 10, "P": 50,
        "Q": 30, "R": 50, "S": 20, "T": 20,
        "U": 40, "V": 50, "W": 20, "X": 17,
        "Y": 20, "Z": 21
    }
    
    # Multi-buy special offers for individual items
    # Format: item -> list of (quantity, special_price), sorted descending by quantity later
    offers = {
        "A": [(5, 200), (3, 130)],
        "B": [(2, 45)],
        "H": [(10, 80), (5, 45)],
        "K": [(2, 120)],
        "P": [(5, 200)],
        "Q": [(3, 80)],
        "V": [(3, 130), (2, 90)]
    }
    
    # "Buy X get Y free" offers:
    # Format: trigger_item -> (required_qty, free_item, free_count)
    free_offers = {
        "E": (2, "B", 1),
        "N": (3, "M", 1),
        "R": (3, "Q", 1),
        "U": (3, "U", 1),
        "F": (3, "F", 1)
    }
    
    # Group discount offer for items S, T, X, Y, Z:
    # "Buy any 3 of (S, T, X, Y, Z) for 45"
    group_items = ["S", "T", "X", "Y", "Z"]
    group_offer_price = 45
    
    # Validate input: if any SKU is invalid, return -1.
    for ch in skus:
        if ch not in prices:
            return -1
    
    # Count all items
    counts = Counter(skus)
    
    # Apply "buy X get Y free" offers first.
    for trigger, (req_qty, free_item, free_count) in free_offers.items():
        if trigger in counts:
            free_items_earned = (counts[trigger] // req_qty) * free_count
            if free_item in counts:
                counts[free_item] = max(0, counts[free_item] - free_items_earned)
            else:
                counts[free_item] = 0

    total = 0

    # Handle group discount for items S, T, X, Y, Z.
    group_list = []
    for item in group_items:
        if item in counts:
            group_list.extend([item] * counts[item])
            # Remove these items from individual processing.
            del counts[item]
    if group_list:
        # Sort the group items in descending order of price so that the highest-priced items are grouped first.
        group_list.sort(key=lambda item: prices[item], reverse=True)
        num_groups = len(group_list) // 3
        total += num_groups * group_offer_price
        remaining = len(group_list) % 3
        if remaining:
            # Charge remaining items at individual prices.
            total += sum(prices[item] for item in group_list[-remaining:])

    # Process remaining items (those not in the group discount)
    for item, count in counts.items():
        if item in offers:
            # Apply multi-buy offers, sorted descending by quantity.
            for offer_qty, offer_price in sorted(offers[item], key=lambda x: x[0], reverse=True):
                num_offers = count // offer_qty
                total += num_offers * offer_price
                count %= offer_qty
        total += count * prices[item]
    
    return total
