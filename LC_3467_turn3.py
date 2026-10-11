class Solution:
    def transformArray(self, nums):
        transformed = []
        for x in nums:
            if x > 0:
                transformed.append(0 if x % 2 == 0 else 1)
            else:
                transformed.append(x)
        transformed.sort()
        return transformed