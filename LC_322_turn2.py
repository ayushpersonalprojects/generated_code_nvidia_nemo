class Solution:
    def coinChange(self, coins, amount):
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

        INF = amount + 1  # larger than any possible answer
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            if coin <= 0:
                continue  # ignore non‑positive denominations
            for cur in range(coin, amount + 1):
                if dp[cur - coin] + 1 < dp[cur]:
                    dp[cur] = dp[cur - coin] + 1

        return dp[amount] if dp[amount] != INF else -1