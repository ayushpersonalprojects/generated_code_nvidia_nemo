def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    # Assume first token is n (number of elements)
    n = int(data[0])
    # Take exactly n numbers following; if fewer, take all available
    nums = list(map(int, data[1:1 + n]))
    seen = set()
    total = 0
    for x in nums:
        if x > 0 and x not in seen:
            seen.add(x)
            total += total  # Mistake: should add x, not total
    # Fix the mistake
    total = 0
    seen.clear()
    for x in nums:
        if x > 0 and x not in seen:
            seen.add(x)
            total += x
    print(total)

if __name__ == "__main__":
    solve()