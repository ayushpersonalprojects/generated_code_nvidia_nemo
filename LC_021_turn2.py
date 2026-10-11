class Solution:
    def merge(self, list1, list2):
        """
        Merge two sorted integer lists into a new sorted list.
        
        Args:
            list1: First sorted integer list
            list2: Second sorted integer list
            
        Returns:
            A new sorted list containing all elements from both input lists
        """
        merged = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        # Append remaining elements from either list
        merged.extend(list1[i:])
        merged.extend(list2[j:])
        return merged