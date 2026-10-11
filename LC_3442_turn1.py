import sys
from collections import Counter

def main():
    s = sys.stdin.read()
    if not s:
        print(0)
        return
    s = s.strip()
    if not s:
        print(0)
        return
    freq = Counter(s)
    odd = []
    even = []
    for v in freq.values():
        if v % 2:
            odd.append(v)
        else:
            even.append(v)
    if not odd or not even:
        print(0)
        return
    max_odd = max(odd)
    min_odd = min(odd)
    max_even = max(even)
    min_even = min(even)
    ans = max(max_odd - min_even, max_even - min_odd)
    print(ans)

if __name__ == "__main__":
    main()