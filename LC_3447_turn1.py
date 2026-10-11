import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    m = int(next(it))
    queries = [int(next(it)) for _ in range(m)]

    max_val = max(arr) if arr else 0
    INF = 10**9

    # earliest index for each exact value (non-zero)
    first_idx = [INF] * (max_val + 1)
    earliest_zero_idx = INF
    for idx, val in enumerate(arr):
        if val == 0:
            if idx < earliest_zero_idx:
                earliest_zero_idx = idx
        else:
            if idx < first_idx[val]:
                first_idx[val] = idx

    # answer for each divisor d: earliest index of an element divisible by d
    ans = [INF] * (max_val + 1)
    for d in range(1, max_val + 1):
        best = INF
        # iterate multiples of d
        for mult in range(d, max_val + 1, d):
            if first_idx[mult] < best:
                best = first_idx[mult]
        ans[d] = best

    # incorporate zero (if any) because 0 is divisible by any positive d
    if earliest_zero_idx != INF:
        for d in range(1, max_val + 1):
            if earliest_zero_idx < ans[d]:
                ans[d] = earliest_zero_idx

    out_lines = []
    for k in queries:
        if k <= 0:
            out_lines.append("-1")
            continue
        if k > max_val:
            # if k exceeds max array value, only zero could satisfy
            if earliest_zero_idx != INF:
                out_lines.append(str(earliest_zero_idx))
            else:
                out_lines.append("-1")
        else:
            res = ans[k]
            out_lines.append(str(res) if res != INF else "-1")

    sys.stdout.write(" ".join(out_lines))

if __name__ == "__main__":
    solve()