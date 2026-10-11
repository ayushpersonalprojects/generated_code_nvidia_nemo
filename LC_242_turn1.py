from collections import Counter

def same_letters(s1: str, s2: str) -> bool:
    """Return True if s1 and s2 contain the same letters with the same multiplicities, regardless of order."""
    return Counter(s1) == Counter(s2)