class Solution:
    def transformArray(self, arr):
        transformed = []
        for x in arr:
            if x > 0:
                transformed.append(0 if x % 2 == 0 else 1)
            else:
                transformed.append(x)
        transformed.sort()
        return transformed