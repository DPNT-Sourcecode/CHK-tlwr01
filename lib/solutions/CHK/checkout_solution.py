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
    offers = {
        "A": [(5, 200), (3, 130)],
        "B": [(2, 45)],
        "H": [(10, 80), (5, 45)],
        "K": [(2, 120)],
        "P": [(5, 200)],
        "Q": [(3, 80)],
        "V": [(3, 130), (2, 90)]
    }
    
    # "Buy X get Y free" offers
    free_offers = {
        "E": (2, "B", 1),
        "N": (3, "M", 1),
        "R": (3, "Q", 1),
        "U": (4, "U", 1),  # For U: only every 4 U's gives one free.
        "F": (3, "F", 1)
    }
    
    # Group discount for items S, T, X, Y, Z: buy any 3 for 45
    group_items = ["S", "T", "X", "Y", "Z"]
    group_offer_price = 45
    
    # Validate input: return -1 if any character is invalid
    for ch in skus:
        if ch not in prices:
            return -1
    
    # Count items
    counts = Counter(skus)
    
    # Apply "buy X get Y free" offers
    for trigger, (req_qty, free_item, free_count) in free_offers.items():
        if trigger in counts:
            free_items_earned = (counts[trigger] // req_qty) * free_count
            if free_item in counts:
                counts[free_item] = max(0, counts[free_item] - free_items_earned)
            else:
                counts[free_item] = 0
    
    total = 0
    
    # Process group discount for S, T, X, Y, Z
    group_list = []
    for item in group_items:
        if item in counts:
            group_list.extend([item] * counts[item])
            del counts[item]
    if group_list:
        group_list.sort(key=lambda item: prices[item], reverse=True)
        num_groups = len(group_list) // 3
        total += num_groups * group_offer_price
        remaining = len(group_list) % 3
        if remaining:
            total += sum(prices[item] for item in group_list[-remaining:])
    
    # Process remaining items with multi-buy offers
    for item, count in counts.items():
        if item in offers:
            for offer_qty, offer_price in sorted(offers[item], key=lambda x: x[0], reverse=True):
                num_offers = count // offer_qty
                total += num_offers * offer_price
                count %= offer_qty
        total += count * prices[item]
    
    return total
