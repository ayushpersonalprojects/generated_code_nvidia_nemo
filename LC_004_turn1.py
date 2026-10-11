def findMedianSortedArrays(nums1, nums2):
    """
    Returns the median of two sorted arrays in O(log(min(len(nums1), len(nums2)))) time.
    """
    # Ensure nums1 is the smaller array for binary search
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total = m + n
    half = (total + 1) // 2  # left part size

    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2          # partition in nums1
        j = half - i                # partition in nums2

        # Edge values
        left1  = float('-inf') if i == 0 else nums1[i - 1]
        right1 = float('inf')  if i == m else nums1[i]
        left2  = float('-inf') if j == 0 else nums2[j - 1]
        right2 = float('inf')  if j == n else nums2[j]

        if left1 <= right2 and left2 <= right1:
            # Correct partition
            if total % 2:
                return max(left1, left2)
            else:
                return (max(left1, left2) + min(right1, right2)) / 2.0
        elif left1 > right2:
            hi = i - 1
        else:
            lo = i + 1

    raise ValueError("Input arrays are not sorted or invalid.")