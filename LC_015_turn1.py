def three_sum(nums):
    """
    Return all unique triplets [a, b, c] in nums such that a + b + c == 0.
    The result contains no duplicate triplets.
    """
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicates for the second and third elements
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return res