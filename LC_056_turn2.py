class Solution:
    def merge(self, intervals):
        """
        Merge overlapping intervals.

        Args:
            intervals (List[List[int]]): List of [start, end] intervals.

        Returns:
            List[List[int]]: List of merged, non-overlapping intervals sorted by start.
        """
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
                
        return merged