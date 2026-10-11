import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    a = [int(next(it)) for _ in range(n)]

    lo = min(a)
    hi = lo + k + 1  # exclusive upper bound

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        needed = 0
        for val in a:
            if val < mid:
                needed += mid - val
                if needed > k:  # early exit if already exceeds k
                    break
        if needed <= k:
            lo = mid
        else:
            hi = mid

    print(lo)


if __name__ == "__main__":
    solve()