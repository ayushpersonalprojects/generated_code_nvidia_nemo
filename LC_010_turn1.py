def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[m][n] = True  # empty pattern matches empty string

    for i in range(m, -1, -1):
        for j in range(n - 1, -1, -1):
            first_match = i < m and (p[j] == s[i] or p[j] == '.')
            if j + 1 < n and p[j + 1] == '*':
                dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
            else:
                dp[i][j] = first_match and dp[i + 1][j + 1]
    return dp[0][0]

# Example usage:
# print(isMatch("aa", "a"))        # False
# print(isMatch("aa", "a*"))       # True
# print(isMatch("ab", ".*"))       # True
# print(isMatch("aab", "c*a*b"))   # True
# print(isMatch("mississippi", "mis*is*p*."))  # False