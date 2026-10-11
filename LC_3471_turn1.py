def largest_unique_in_groups(groups):
    """
    Returns the largest integer that appears in exactly one of the given groups.
    If no such integer exists, returns -1.

    Parameters:
    groups (list of list of int): A list where each element is a group (list) of integers.

    Returns:
    int: The largest integer occurring in exactly one group, or -1 if none.
    """
    # Dictionary to count in how many groups each integer appears
    appearance_count = {}

    for group in groups:
        # Use a set to ignore duplicates within the same group
        unique_in_group = set(group)
        for num in unique_in_group:
            appearance_count[num] = appearance_count.get(num, 0) + 1

    # Filter integers that appear in exactly one group
    candidates = [num for num, cnt in appearance_count.items() if cnt == 1]

    return max(candidates) if candidates else -1


# Example usage (can be removed or commented out when integrating elsewhere)
if __name__ == "__main__":
    examples = [
        ([[1, 2, 3], [2, 3, 4], [5, 6]], 6),
        ([[1, 2], [2, 3], [1, 3]], -1),
        ([], -1),
        ([[], [1, 1, 2], [2, 3]], 3),
        ([[7, 7, 7], [7, 8], [9]], 9),
    ]

    for groups, expected in examples:
        result = largest_unique_in_groups(groups)
        print(f"groups={groups} => {result} (expected {expected})")