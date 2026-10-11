def subsets(nums):
    """
    Return all distinct subsets (the power set) of a list of distinct integers.

    Parameters
    ----------
    nums : List[int]
        A list of distinct integers.

    Returns
    -------
    List[List[int]]
        A list containing all possible subsets. Each subset is represented as a list.
    """
    result = []

    def backtrack(start, current):
        # Append a copy of the current subset
        result.append(current[:])
        # Explore further elements
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()  # backtrack

    backtrack(0, [])
    return result


# Example usage:
if __name__ == "__main__":
    example = [1, 2, 3]
    print(subsets(example))
    # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]