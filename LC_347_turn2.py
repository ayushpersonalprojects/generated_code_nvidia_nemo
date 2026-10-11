from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k <= 0:
            return []
        freq = Counter(nums)
        most_common = freq.most_common(k)
        return [elem for elem, _ in most_common]