import sys
import math

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    A = [next(it) for _ in range(n)]
    m = next(it)
    T = [next(it) for _ in range(m)]

    if m == 0:
        print(0)
        return

    full_mask = (1 << m) - 1
    size = 1 << m

    # LCM for each mask
    lcm_mask = [0] * size
    lcm_mask[0] = 1
    for mask in range(1, size):
        lsb = mask & -mask
        bit = (lsb.bit_length() - 1)
        prev = mask ^ lsb
        a = lcm_mask[prev]
        b = T[bit]
        lcm_mask[mask] = a // math.gcd(a, b) * b

    # Cost for each element and each mask
    cost = [[0] * size for _ in range(n)]
    for i in range(n):
        ai = A[i]
        ci = cost[i]
        for mask in range(size):
            l = lcm_mask[mask]
            mult = ((ai + l - 1) // l) * l
            ci[mask] = mult - ai

    INF = 10 ** 18
    dp = [INF] * size
    dp[0] = 0

    for i in range(n):
        ci = cost[i]
        ndp = dp[:]  # start with not using this element
        for mask in range(size):
            base = dp[mask]
            if base == INF:
                continue
            rem = full_mask ^ mask
            sub = rem
            while True:
                new_mask = mask | sub
                val = base + ci[sub]
                if val < ndp[new_mask]:
                    ndp[new_mask] = val
                if sub == 0:
                    break
                sub = (sub - 1) & rem
        dp = ndp

    print(dp[full_mask])

if __name__ == "__main__":
    solve()