from typing import List

class Solution:
    def sumOfArray(self, nums: List[int], k: int) -> int:
        """
        Return the sum of elements nums[i] such that both neighbors at distance k
        (i-k and i+k) exist and are strictly smaller than nums[i].
        """
        n = len(nums)
        total = 0
        if k < 0:
            raise ValueError("k must be non-negative")
        for i in range(n):
            left = i - k
            right = i + k
            if left >= 0 and right < n:
                if nums[left] < nums[i] and nums[right] < nums[i]:
                    total += nums[i]
        return total