def coin_change(coins, amount):
    # Initialize the dp array with a size of amount + 1, filled with a large number
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # No coins needed to make amount 0

    # Iterate through each coin
    for coin in coins:
        # Update the dp array for each amount from the value of the coin to the target amount
        for j in range(coin, amount + 1):
            if dp[j - coin] != float('inf'):
                dp[j] = min(dp[j], dp[j - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))  # Output: 3
