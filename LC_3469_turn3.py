class Solution:
    def minRemovalCost(self, nums):
        """
        Returns the minimum total cost to remove all elements.
        Removing an element nums[k] when its current left neighbor is nums[i]
        and right neighbor is nums[j] costs nums[i] * nums[k] * nums[j].
        After removal, the left and right neighbors become adjacent.
        This problem is equivalent to finding the minimum score triangulation
        of a polygon with vertex values given in `nums`.
        """
        n = len(nums)
        if n < 3:
            return 0

        # dp[i][j] = minimum cost to triangulate the sub-polygon from vertex i to j (inclusive)
        dp = [[0] * n for _ in range(n)]

        # Consider intervals of increasing length (j - i)
        for length in range(2, n):          # length = j - i
            for i in range(0, n - length):
                j = i + length
                best = float('inf')
                # Try every possible vertex k between i and j as the last to form a triangle (i, k, j)
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j]
                    if cost < best:
                        best = cost
                dp[i][j] = best

        return dp[0][n - 1]