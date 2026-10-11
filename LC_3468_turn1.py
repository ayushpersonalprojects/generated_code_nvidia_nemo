import sys

def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    L = [next(it) for _ in range(n)]
    R = [next(it) for _ in range(n)]
    remaining = list(it)

    MOD = 10**9 + 7

    # Determine adjacent-difference constraints
    if len(remaining) == 0:
        # No constraints: independent choices per position
        ans = 1
        for i in range(n):
            ans = ans * (R[i] - L[i] + 1) % MOD
        print(ans)
        return
    elif len(remaining) == 1:
        K = remaining[0]
        lowDiff = [-K] * (n - 1)
        highDiff = [K] * (n - 1)
    elif len(remaining) == n - 1:
        maxDiff = remaining
        lowDiff = [-d for d in maxDiff]
        highDiff = maxDiff
    elif len(remaining) == 2 * (n - 1):
        lowDiff = remaining[:n - 1]
        highDiff = remaining[n - 1:2 * (n - 1)]
    else:
        # Fallback: treat first number as uniform K
        K = remaining[0]
        lowDiff = [-K] * (n - 1)
        highDiff = [K] * (n - 1)

    if n == 1:
        print((R[0] - L[0] + 1) % MOD)
        return

    # DP over value ranges
    low_prev = L[0]
    high_prev = R[0]
    size_prev = high_prev - low_prev + 1
    dp_prev = [1] * size_prev  # all values in [L0, R0] are possible for first element

    for idx in range(1, n):
        low_curr = L[idx]
        high_curr = R[idx]
        ld = low_diff[idx - 1]
        hd = high_diff[idx - 1]
        size_curr = high_curr - low_curr + 1

        # Prefix sums of dp_prev
        pref = [0] * (size_prev + 1)
        acc = 0
        for i in range(size_prev):
            acc += dp_prev[i]
            if acc >= MOD:
                acc -= MOD
            pref[i + 1] = acc

        dp_curr = [0] * size_curr
        for v in range(low_curr, high_curr + 1):
            left = v - hd
            right = v - ld
            if left < low_prev:
                left = low_prev
            if right > high_prev:
                right = high_prev
            if left > right:
                total = 0
            else:
                li = left - low_prev
                ri = right - low_prev
                total = pref[ri + 1] - pref[li]
                if total < 0:
                    total += MOD
            dp_curr[v - low_curr] = total % MOD

        dp_prev = dp_curr
        low_prev = low_curr
        high_prev = high_curr
        size_prev = size_curr

    ans = sum(dp_prev) % MOD
    print(ans)

if __name__ == "__main__":
    solve()