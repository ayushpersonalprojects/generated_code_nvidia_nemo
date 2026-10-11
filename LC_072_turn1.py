def edit_distance(s1: str, s2: str) -> int:
    """
    Compute the Levenshtein distance between two strings.
    Returns the minimum number of insertions, deletions, or substitutions
    required to transform s1 into s2.
    """
    if len(s1) < len(s2):
        s1, s2 = s2, s1  # ensure s1 is the longer string for space optimization

    previous = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1, 1):
        current = [i] + [0] * len(s2)
        for j, c2 in enumerate(s2, 1):
            insert_cost = current[j - 1] + 1
            delete_cost = previous[j] + 1
            replace_cost = previous[j - 1] + (c1 != c2)
            current[j] = min(insert_cost, delete_cost, replace_cost)
        previous = current
    return previous[-1]