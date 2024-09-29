# Class to represent an item with value and weight
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Function to get the maximum value of the knapsack
def fractional_knapsack(W, items):
    # Sorting items by value to weight ratio (in decreasing order)
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0.0  # Variable to store the total value
    for item in items:
        if W == 0:  # If the knapsack is full
            break
        # If the item can be fully added
        if item.weight <= W:
            W -= item.weight
            total_value += item.value
        else:
            # If the item can be partially added
            total_value += item.value * (W / item.weight)
            W = 0  # The knapsack is full

    return total_value

# Example usage
if __name__ == "__main__":
    W = 50  # Weight capacity of the knapsack
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]  # (value, weight) pairs
    max_value = fractional_knapsack(W, items)
    print("Maximum value we can obtain =", max_value)
