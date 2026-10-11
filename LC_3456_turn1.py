def has_maximal_k_substring(s: str, k: int) -> bool:
    """
    Returns True if there exists a substring of length k consisting of identical
    characters that cannot be extended to the left or right while keeping all
    characters identical (i.e., it is a maximal run of exactly k identical chars).
    """
    if k <= 0:
        return False
    n = len(s)
    if k > n:
        return False

    i = 0
    while i < n:
        # start of a run
        run_char = s[i]
        j = i
        while j < n and s[j] == run_char:
            j += 1
        run_len = j - i
        if run_len == k:
            # run is maximal by construction (cannot extend left/right)
            return True
        i = j  # move to next run
    return False


# Example usage:
if __name__ == "__main__":
    assert has_maximal_k_substring("aaabbcaaa", 3) == True   # "aaa" at start or end
    assert has_maximal_k_substring("aaabbcaaa", 2) == False  # no maximal run of exactly 2
    assert has_maximal_k_substring("abcccba", 3) == True     # "ccc"
    assert has_maximal_k_substring("abcccba", 4) == False
    assert has_maximal_k_substring("a", 1) == True
    assert has_maximal_k_substring("", 1) == False
    print("All tests passed.")