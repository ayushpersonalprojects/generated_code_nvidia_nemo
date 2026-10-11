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

    # Determine adjacent-difference constraints
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
    elif len(rem) == n - 1:         # per-edge upper bound, lower = -upper
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

    # DP over possible values, keeping only the current interval
    low_prev, high_prev = L[0], R[0]
    size_prev = high_prev - low_prev + 1
    dp_prev = [1] * size_prev          # all values in [L0,R0] are possible for a0

    for idx in range(1, n):
        ld = low_diff[idx - 1]
        hd = high_diff[idx - 1]
        low_curr, high_curr = L[idx], R[idx]

        # The feasible values for a_idx must satisfy:
        #   a_idx - hd <= a_{idx-1} <= a_idx - ld
        # and a_{idx-1} must be in [low_prev, high_prev]
        # => a_idx must be in [low_prev + ld, high_prev + hd]
        new_low = max(low_curr, low_prev + ld)
        new_high = min(high_curr, high_prev + hd)
        if new_low > new_high:
            print(0)
            return

        size_curr = new_high - new_low + 1
        # Prefix sums of dp_prev (extended with zeros outside [low_prev,high_prev])
        pref = [0] * (size_prev + 1)
        acc = 0
        for i in range(size_prev):
            acc += dp_prev[i]
            if acc >= MOD:
                acc -= MOD
            pref[i + 1] = acc

        dp_curr = [0] * size_curr
        # For each possible value v in [new_low, new_high]
        for offset, v in enumerate(range(new_low, new_high + 1)):
            left = v - hd          # minimal a_{idx-1}
            right = v - ld         # maximal a_{idx-1}
            # Clamp to previous domain
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
            dp_curr[offset] = total % MOD

        # Prepare for next iteration
        dp_prev = dp_curr
        low_prev, high_prev = new_low, new_high
        size_prev = size_curr

    ans = sum(dp_prev) % MOD
    print(ans)


if __name__ == "__main__":
    solve()