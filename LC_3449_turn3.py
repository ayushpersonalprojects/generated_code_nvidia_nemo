import sys, bisect

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    # Try to interpret first number as test case count
    t = data[0]
    idx = 1
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

        arr.sort()
        pref = [0]
        for v in arr:
            pref.append(pref[-1] + v)

        lo = arr[0]
        hi = lo + k + 1          # exclusive upper bound
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            cnt = bisect.bisect_left(arr, mid)   # number of elements < mid
            need = mid * cnt - pref[cnt]
            if need <= k:
                lo = mid
            else:
                hi = mid
        answers.append(str(lo))

    if ok and idx == len(data):
        sys.stdout.write("\n".join(answers))
        return

    # Fallback: single test case (no leading T)
    idx = 0
    n = data[idx]
    k = data[idx + 1]
    idx += 2
    arr = data[idx:idx + n]

    arr.sort()
    pref = [0]
    for v in arr:
        pref.append(pref[-1] + v)

    lo = arr[0]
    hi = lo + k + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        cnt = bisect.bisect_left(arr, mid)
        need = mid * cnt - pref[cnt]
        if need <= k:
            lo = mid
        else:
            hi = mid
    sys.stdout.write(str(lo))

if __name__ == "__main__":
    solve()