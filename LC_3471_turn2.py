class Solution:
    def largestInteger(self, groups):
        """
        Returns the largest integer that appears in exactly one of the given groups.
        If no such integer exists, returns -1.

        Parameters:
        groups (List[List[int]]): A list where each element is a group (list) of integers.

        Returns:
        int: The largest integer occurring in exactly one group, or -1 if none.
        """
        appearance_count = {}
        for group in groups:
            # Use a set to ignore duplicates within the same group
            for num in set(group):
                appearance_count[num] = appearance_count.get(num, 0) + 1

        # Filter integers that appear in exactly one group
        candidates = [num for num, cnt in appearance_count.items() if cnt == 1]

        return max(candidates) if candidates else -1