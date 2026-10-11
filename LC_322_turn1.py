def coinChange(coins, amount):
    """
    Returns the minimum number of coins needed to make up the given amount.
    If it's not possible, returns -1.

    Parameters:
    coins (List[int]): List of distinct coin denominations.
    amount (int): Target amount.

    Returns:
    int: Minimum number of coins required, or -1 if impossible.
    """
    if amount < 0:
        return -1
    if amount == 0:
        return 0

    # Initialize DP array with a value larger than any possible answer.
    INF = amount + 1  # because the worst case is using all 1‑value coins.
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        if coin <= 0:
            continue  # ignore non‑positive denominations
        for cur_amount in range(coin, amount + 1):
            if dp[cur_amount - coin] + 1 < dp[cur_amount]:
                dp[cur_amount] = dp[cur_amount - coin] + 1

    return dp[amount] if dp[amount] != INF else -1


# Example usage:
if __name__ == "__main__":
    # Example 1
    print(coinChange([1, 2, 5], 11))  # Output: 3 (5+5+1)

    # Example 2
    print(coinChange([2], 3))         # Output: -1

    # Example 3
    print(coinChange([1], 0))         # Output: 0