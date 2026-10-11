def sum_peaks(arr, k):
    """
    Return the sum of elements arr[i] such that both neighbors at distance k
    (i-k and i+k) exist and are strictly smaller than arr[i].
    """
    n = len(arr)
    total = 0
    if k < 0:
        raise ValueError("k must be non-negative")
    for i in range(n):
        left = i - k
        right = i + k
        if left >= 0 and right < n:
            if arr[left] < arr[i] and arr[right] < arr[i]:
                total += arr[i]
    return total