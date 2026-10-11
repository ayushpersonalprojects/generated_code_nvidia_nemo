def minRemovalCost(nums):
    """
    Returns the minimum total cost to remove all elements from the array.
    Removing an element nums[k] when its current left neighbor is nums[i]
    and right neighbor is nums[j] costs nums[i] * nums[k] * nums[j].
    After removal, the left and right neighbors become adjacent.
    This is equivalent to the minimum‑score version of the Burst Balloons problem.
    """
    if not nums:
        return 0

    # Add virtual boundaries with value 1 to simplify calculations.
    arr = [1] + nums + [1]
    n = len(arr)

    # dp[i][j] = minimum cost to remove all elements strictly between i and j.
    dp = [[0] * n for _ in range(n)]

    # Consider intervals of increasing length.
    for length in range(2, n):          # length = j - i
        for i in range(0, n - length):
            j = i + length
            best = float('inf')
            # Try every possible last removal k in (i, j).
            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j]
                if cost < best:
                    best = cost
            dp[i][j] = best

    return dp[0][n - 1]