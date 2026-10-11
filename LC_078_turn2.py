class Solution:
    def subsets(self, nums):
        """
        Return all distinct subsets (the power set) of a list of distinct integers.

        Parameters
        ----------
        nums : List[int]
            A list of distinct integers.

        Returns
        -------
        List[List[int]]
            A list containing all possible subsets. Each subset is represented as a list.
        """
        result = []

        def backtrack(start, current):
            # Append a copy of the current subset
            result.append(current[:])
            # Explore further elements
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()  # backtrack

        backtrack(0, [])
        return result