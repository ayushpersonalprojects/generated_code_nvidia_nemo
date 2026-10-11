class Solution:
    def find_adjacent_pair(self, s: str) -> str:
        from collections import Counter
        freq = Counter(ch for ch in s if ch.isdigit())
        for i in range(len(s) - 1):
            a, b = s[i], s[i + 1]
            if a.isdigit() and b.isdigit() and a != b:
                if freq.get(a, 0) == int(a) and freq.get(b, 0) == int(b):
                    return a + b
        return ""