def uniquePaths(m: int, n: int) -> int:
    """Return number of unique paths from top‑left to bottom‑right in an m×n grid,
    moving only right or down."""
    from math import comb
    # Total steps = (m-1) down + (n-1) right = m+n-2
    # Choose positions of down moves (or right moves)
    return comb(m + n - 2, m - 1)