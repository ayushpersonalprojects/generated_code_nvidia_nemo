from collections import Counter
from typing import List, Any

class Solution:
    def maxStudentsOnBench(self, pairs: List[List[Any]]) -> int:
        if not pairs:
            return 0
        bench_counts = Counter(bench for _, bench in pairs)
        return max(bench_counts.values())