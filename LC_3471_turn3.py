class Solution:
    def largestInteger(self, nums):
        """
        Returns the largest integer that appears exactly once in the given list.
        If no such integer exists, returns -1.

        Parameters:
        nums (List[int]): List of integers.

        Returns:
        int: The largest integer with frequency 1, or -1 if none.
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Collect numbers that appear exactly once
        unique_nums = [num for num, cnt in freq.items() if cnt == 1]

        return max(unique_nums) if unique_nums else -1