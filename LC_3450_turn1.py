from collections import Counter
from typing import List, Tuple, Any

def max_students_on_bench(pairs: List[Tuple[Any, Any]]) -> int:
    """
    Given a list of pairs (student, bench), return the largest number of students
    sharing the same bench.

    Parameters
    ----------
    pairs : List[Tuple[Any, Any]]
        Each tuple represents a student and the bench they sit on.
        The first element is the student identifier (unused for counting),
        the second element is the bench identifier.

    Returns
    -------
    int
        The maximum number of students on any single bench. Returns 0 if the
        input list is empty.
    """
    if not pairs:
        return 0

    # Count how many times each bench appears
    bench_counts = Counter(bench for _, bench in pairs)

    # Return the highest count
    return max(bench_counts.values())