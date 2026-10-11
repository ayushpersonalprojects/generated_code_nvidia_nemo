from collections import deque
from typing import List, Set

def ladder_length(start: str, end: str, dictionary: List[str]) -> int:
    """
    Returns the number of one-letter transformations in the shortest
    valid chain from start to end using words from dictionary.
    If no such chain exists, returns 0.
    """
    word_set: Set[str] = set(dictionary)
    # Ensure the end word is considered reachable
    word_set.add(end)

    if start == end:
        return 0  # No transformation needed

    queue = deque([(start, 0)])  # (current_word, transformations_so_far)
    visited: Set[str] = {start}

    word_len = len(start)

    while queue:
        current, steps = queue.popleft()
        # Generate all possible one-letter mutations
        for i in range(word_len):
            for c in map(chr, range(ord('a'), ord('z') + 1)):
                if c == current[i]:
                    continue
                neighbor = current[:i] + c + current[i+1:]
                if neighbor not in word_set or neighbor in visited:
                    continue
                if neighbor == end:
                    return steps + 1  # Found the end word
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))

    # No transformation sequence found
    return 0