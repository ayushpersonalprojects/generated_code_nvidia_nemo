from collections import Counter
from typing import List, Any

class Solution:
    def maxStudentsOnBench(self, students: List[List[Any]]) -> int:
        if not students:
            return 0
        bench_counts = Counter(bench for _, bench in students)
        return max(bench_counts.values())