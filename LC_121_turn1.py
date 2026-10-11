def maxProfit(prices):
    """
    Returns the maximum profit from a single buy-sell transaction.
    If no profit is possible, returns 0.
    """
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        # Potential profit if we sell today
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
        # Update the minimum price seen so far
        if price < min_price:
            min_price = price

    return max_profit