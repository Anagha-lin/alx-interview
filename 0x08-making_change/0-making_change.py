#!/usr/bin/python3

def makeChange(coins, total):
    """Calculate the fewest number of coins needed to meet total."""
    if total <= 0:
        return 0
    
    # Create a list to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make total 0

    # Iterate over each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Check if total can be made with available coins
    return dp[total] if dp[total] != float('inf') else -1

if __name__ == "__main__":
    # Example usage
    print(makeChange([1, 2, 25], 37))  # Expected output: 4 (25 + 10 + 2)
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1

