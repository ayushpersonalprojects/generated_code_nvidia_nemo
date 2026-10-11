def solve():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    # Try to interpret first number as number of test cases
    T = data[0]
    ptr = 1
    answers = []
    ok = True
    for _ in range(T):
        if ptr >= len(data):
            ok = False
            break
        n = data[ptr]
        ptr += 1
        if ptr + n > len(data):
            ok = False
            break
        arr = data[ptr:ptr + n]
        ptr += n
        seen = set()
        total = 0
        for x in arr:
            if x > 0 and x not in seen:
                seen.add(x)
                total += x
        answers.append(total)
    if ok and ptr == len(data):
        sys.stdout.write("\n".join(map(str, answers)))
        return

    # Fallback: treat input as a sequence of (n, n numbers) without leading T
    ptr = 0
    answers = []
    while ptr < len(data):
        n = data[ptr]
        ptr += 1
        if ptr + n > len(data):
            break  # incomplete test case, ignore
        arr = data[ptr:ptr + n]
        ptr += n
        seen = set()
        total = 0
        for x in arr:
            if x > 0 and x not in seen:
                seen.add(x)
                total += x
        answers.append(total)

    sys.stdout.write("\n".join(map(str, answers)))

if __name__ == "__main__":
    solve()