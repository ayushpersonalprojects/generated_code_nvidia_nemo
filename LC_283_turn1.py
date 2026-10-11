def move_zeros(arr):
    """Return a new list with all zeros moved to the end, preserving order of non-zero elements."""
    nonzeros = [x for x in arr if x != 0]
    zeros_count = len(arr) - len(nonzeros)
    return nonzeros + [0] * zeros_count

if __name__ == "__main__":
    # Example test cases
    print(move_zeros([0, 1, 0, 3, 12]))          # [1, 3, 12, 0, 0]
    print(move_zeros([1, 2, 3, 0, 0, 0]))       # [1, 2, 3, 0, 0, 0]
    print(move_zeros([0, 0, 0]))                # [0, 0, 0]
    print(move_zeros([4, 5, 6]))                # [4, 5, 6]
    print(move_zeros([]))                       # []