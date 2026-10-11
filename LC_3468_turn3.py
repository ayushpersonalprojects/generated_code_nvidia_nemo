import sys

MOD = 10**9 + 7

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    L = [next(it) for _ in range(n)]
    R = [next(it) for _ in range(n)]
    rem = list(it)

    # ----- determine adjacent-difference constraints -----
    if not rem:                     # no constraints
        ans = 1
        for i in range(n):
            ans = ans * (R[i] - L[i] + 1) % MOD
        print(ans)
        return
    if len(rem) == 1:               # uniform bound K
        K = rem[0]
        low_diff = [-K] * (n - 1)
        high_diff = [K] * (n - 1)
    elif len(rem) == n - 1:         # per‑edge upper bound, lower = -upper
        max_diff = rem
        low_diff = [-d for d in max_diff]
        high_diff = max_diff
    elif len(rem) == 2 * (n - 1):   # explicit lower and upper per edge
        low_diff = rem[:n - 1]
        high_diff = rem[n - 1:2 * (n - 1)]
    else:                           # fallback: treat first number as uniform K
        K = rem[0]
        low_diff = [-K] * (n - 1)
        high_diff = [K] * (n - 1)

    if n == 1:
        print((R[0] - L[0] + 1) % MOD)
        return

    # ----- DP with sliding‑window sums -----
    low_prev, high_prev = L[0], R[0]
    size_prev = high_prev - low_prev + 1
    dp_prev = [1] * size_prev                     # dp for a0

    for idx in range(1, n):
        ld = low_diff[idx - 1]
        hd = high_diff[idx - 1]
        low_cur, high_cur = L[idx], R[idx]

        # feasible values for a_idx after applying the difference constraint
        new_low = max(low_cur, low_prev + ld)
        new_high = min(high_cur, high_prev + hd)
        if new_low > new_high:
            print(0)
            return

        size_cur = new_high - new_low + 1

        # prefix sums of dp_prev (indices 0..size_prev)
        pref = [0] * (size_prev + 1)
        acc = 0
        for i in range(size_prev):
            acc += dp_prev[i]
            if acc >= MOD:
                acc -= MOD
            pref[i + 1] = acc

        dp_cur = [0] * size_cur
        # compute each dp_cur[v] = sum_{u in [v-hd, v-ld]} dp_prev[u]
        for offset in range(size_cur):
            v = new_low + offset
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
            dp_cur[offset] = total

        # prepare for next iteration
        dp_prev = dp_cur
        low_prev, high_prev = new_low, new_high
        size_prev = size_cur

    ans = sum(dp_prev) % MOD
    print(ans)


if __name__ == "__main__":
    solve()