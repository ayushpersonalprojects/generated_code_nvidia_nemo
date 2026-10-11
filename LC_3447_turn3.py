import sys
import math

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    m = int(next(it))
    queries = [int(next(it)) for _ in range(m)]

    INF = n + 5
    first_zero_idx = INF
    for i, v in enumerate(arr):
        if v == 0:
            first_zero_idx = i
            break

    # max non-zero value
    max_val = 0
    for v in arr:
        if v > max_val:
            max_val = v

    # If all zeros, answer directly from zero index
    if max_val == 0:
        out = []
        for k in queries:
            if k <= 0:
                out.append("-1")
            else:
                out.append(str(first_zero_idx) if first_zero_idx != INF else "-1")
        sys.stdout.write(" ".join(out))
        return

    # Decide method based on max_val size
    THRESHOLD = 2_000_000  # adjust if needed
    if max_val <= THRESHOLD:
        # Sieve over multiples
        first_idx = [INF] * (max_val + 1)
        for i, v in enumerate(arr):
            if v != 0 and first_idx[v] > i:
                first_idx[v] = i

        ans = [INF] * (max_val + 1)
        for d in range(1, max_val + 1):
            best = INF
            for mult in range(d, max_val + 1, d):
                if first_idx[mult] < best:
                    best = first_idx[mult]
            ans[d] = best

        if first_zero_idx != INF:
            for d in range(1, max_val + 1):
                if first_zero_idx < ans[d]:
                    ans[d] = first_zero_idx

        out = []
        for k in queries:
            if k <= 0:
                out.append("-1")
            elif k > max_val:
                out.append(str(first_zero_idx) if first_zero_idx != INF else "-1")
            else:
                res = ans[k]
                out.append(str(res) if res != INF else "-1")
        sys.stdout.write(" ".join(out))
    else:
        # Sparse large values: process distinct values via divisor enumeration
        # Precompute primes up to sqrt(max_val)
        limit = int(math.isqrt(max_val)) + 1
        sieve = [True] * (limit + 1)
        primes = []
        for i in range(2, limit + 1):
            if sieve[i]:
                primes.append(i)
                step = i
                start = i * i
                if start > limit:
                    continue
                for j in range(start, limit + 1, step):
                    sieve[j] = False

        def get_divisors(x: int):
            """Return list of divisors of x (x > 0) using prime factorization."""
            orig = x
            factors = []
            for p in primes:
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
            divs = [1]
            for p, exp in factors:
                cur_len = len(divs)
                mul = 1
                for _ in range(exp):
                    mul *= p
                    for i in range(cur_len):
                        divs.append(divs[i] * mul)
            return divs

        first_idx = {}
        for i, v in enumerate(arr):
            if v == 0:
                continue
            if v not in first_idx or i < first_idx[v]:
                first_idx[v] = i

        best_for_div = {}
        for v, idx in first_idx.items():
            for d in get_divisors(v):
                if d not in best_for_div or idx < best_for_div[d]:
                    best_for_div[d] = idx

        if first_zero_idx != INF:
            # zero improves every divisor
            for d in list(best_for_div.keys()):
                if first_zero_idx < best_for_div[d]:
                    best_for_div[d] = first_zero_idx
            # also need to consider divisors that never appeared but zero works
            # we will handle via zero fallback later

        out = []
        for k in queries:
            if k <= 0:
                out.append("-1")
                continue
            ans_idx = best_for_div.get(k, INF)
            if first_zero_idx != INF and first_zero_idx < ans_idx:
                ans_idx = first_zero_idx
            out.append(str(ans_idx) if ans_idx != INF else "-1")
        sys.stdout.write(" ".join(out))

if __name__ == "__main__":
    solve()