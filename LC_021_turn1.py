def merge_sorted_lists(list1, list2):
    """Merge two sorted integer lists into a new sorted list."""
    merged = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    # Append remaining elements
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

# Example usage
if __name__ == "__main__":
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 10]
    print(merge_sorted_lists(a, b))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 10]