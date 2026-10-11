class Solution:
    def longestPalindromicSubsequenceAfterKChanges(self, s: str, k: int) -> int:
        """
        Returns the length of the longest palindromic subsequence that can be obtained
        from `s` after changing at most `k` characters (each change costs 1,
        any character can be changed to any other).
        """
        n = len(s)
        if n == 0:
            return 0

        # dp[l][r][c] = maximum length of a palindromic subsequence
        # obtainable from s[l..r] using at most c changes.
        dp = [[[0] * (k + 1) for _ in range(n)] for __ in range(n)]

        # Base: single characters
        for i in range(n):
            for c in range(k + 1):
                dp[i][i][c] = 1

        # Fill for increasing substring length
        for length in range(2, n + 1):
            for l in range(0, n - length + 1):
                r = l + length - 1
                for c in range(k + 1):
                    # Option 1: skip left character
                    best = dp[l + 1][r][c] if l + 1 <= r else 0
                    # Option 2: skip right character
                    if l <= r - 1 and dp[l][r - 1][c] > best:
                        best = dp[l][r - 1][c]
                    # Option 3: take both ends (make them equal)
                    cost = 0 if s[l] == s[r] else 1
                    if c >= cost:
                        inner_len = 0
                        if l + 1 <= r - 1:
                            inner_len = dp[l + 1][r - 1][c - cost]
                        cand = 2 + inner_len
                        if cand > best:
                            best = cand
                    dp[l][r][c] = best

        return dp[0][n - 1][k]