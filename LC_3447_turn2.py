import sys
import math

def sieve(limit: int):
    """Return list of primes up to limit inclusive."""
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            step = i
            start = i * i
            is_prime[start:limit + 1:step] = [False] * ((limit - start) // step + 1)
    return [i for i, v in enumerate(is_prime) if v]

# Precompute primes up to sqrt(1e9) ~ 31623
_PRIMES = sieve(31623)

def get_divisors(x: int):
    """Return list of all positive divisors of x (x > 0)."""
    # factorize x
    orig = x
    factors = []
    for p in _PRIMES:
        if p * p > x:
            break
        if x % p == 0:
            cnt = 0
            while x % p == 0:
                x //= p
                cnt += 1
            factors.append((p, cnt))
    if x > 1:
        factors.append((x, 1))
    # generate divisors
    divisors = [1]
    for p, exp in factors:
        cur_len = len(divisors)
        mul = 1
        for _ in range(exp):
            mul *= p
            for i in range(cur_len):
                divisors.append(divisors[i] * mul)
    return divisors

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    m = int(next(it))
    queries = [int(next(it)) for _ in range(m)]

    INF = n + 5  # any value > possible index
    first_zero_idx = INF
    for idx, v in enumerate(arr):
        if v == 0:
            first_zero_idx = idx
            break

    # earliest index for each divisor (from non-zero elements)
    earliest = {}
    for idx, val in enumerate(arr):
        if val == 0:
            continue
        for d in get_divisors(val):
            if d not in earliest:          # first occurrence gives smallest index
                earliest[d] = idx

    out = []
    for k in queries:
        if k <= 0:
            out.append("-1")
            continue
        cand = earliest.get(k, INF)
        if first_zero_idx != INF and first_zero_idx < cand:
            cand = first_zero_idx
        out.append(str(cand) if cand != INF else "-1")

    sys.stdout.write(" ".join(out))

if __name__ == "__main__":
    solve()