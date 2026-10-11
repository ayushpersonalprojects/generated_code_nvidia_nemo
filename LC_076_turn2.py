from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need = Counter(t)
        missing = len(t)
        left = start = end = 0
        for right, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            while missing == 0:
                if end == 0 or right - left < end - start:
                    start, end = left, right
                left_char = s[left]
                need[left_char] += 1
                if need[left_char] > 0:
                    missing += 1
                left += 1
        return s[start:end]