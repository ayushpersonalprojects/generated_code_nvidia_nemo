def transform_array(arr):
    transformed = []
    for x in arr:
        if x > 0:
            transformed.append(0 if x % 2 == 0 else 1)
        else:
            transformed.append(x)
    transformed.sort()
    return transformed

if __name__ == "__main__":
    # Example test
    print(transform_array([5, -2, 4, 0, 7, -3]))  # Expected: [-3, -2, 0, 0, 1, 1]