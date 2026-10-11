class Solution:
    def twoSum(self, nums, target):
        """
        Returns the indices of the two distinct elements in `nums` that add up to `target`.
        Assumes exactly one solution exists.
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        # The problem guarantees a solution, so this line is never reached.
        raise ValueError("No two sum solution exists")