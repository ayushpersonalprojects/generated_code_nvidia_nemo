import sys

def max_min_after_ops(n, k, arr):
    lo = min(arr)
    hi = lo + k + 1          # exclusive upper bound
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        needed = 0
        for v in arr:
            if v < mid:
                needed += mid - v
                if needed > k:   # early stop
                    break
        if needed <= k:
            lo = mid
        else:
            hi = mid
    return lo

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    # Try to treat first number as test case count
    idx = 0
    t = data[idx]
    idx += 1
    answers = []
    ok = True
    for _ in range(t):
        if idx + 1 >= len(data):
            ok = False
            break
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        if idx + n > len(data):
            ok = False
            break
        arr = data[idx:idx + n]
        idx += n
        answers.append(str(max_min_after_ops(n, k, arr)))
    if ok and idx == len(data):
        sys.stdout.write("\n".join(answers))
        return

    # Fallback: single test case (no leading T)
    idx = 0
    n = data[idx]
    k = data[idx + 1]
    idx += 2
    arr = data[idx:idx + n]
    ans = max_min_after_ops(n, k, arr)
    sys.stdout.write(str(ans))

if __name__ == "__main__":
    solve()