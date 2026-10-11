import sys

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    results = []
    for _ in range(t):
        n = int(next(it))          # length, not needed for computation
        k = int(next(it))
        s = next(it)
        # Minimal changes so that no run exceeds k identical characters.
        changes = 0
        if s:
            prev = s[0]
            run = 1
            for ch in s[1:]:
                if ch == prev:
                    run += 1
                else:
                    changes += run // (k + 1)
                    run = 1
                    prev = ch
            changes += run // (k + 1)
        results.append(str(changes))
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()