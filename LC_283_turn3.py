from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Move all zeros in nums to the end while maintaining the relative order of non-zero elements.
        Modifies nums in-place and returns the modified list.
        """
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
        return nums