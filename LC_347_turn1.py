from collections import Counter
from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Return the k elements that appear most frequently in nums.
    If k exceeds the number of distinct elements, all distinct elements are returned.
    Order of the returned list is not guaranteed.
    """
    if k <= 0:
        return []
    freq = Counter(nums)
    # most_common returns a list of (element, count) sorted by count descending
    most_common = freq.most_common(k)
    return [elem for elem, _ in most_common]