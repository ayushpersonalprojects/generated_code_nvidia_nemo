import sys

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        k = int(next(it))
        s = next(it)
        # In case the given length does not match the actual string,
        # trust the string's length.
        n = len(s)
        changes = 0
        run = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                run += 1
            else:
                changes += run // (k + 1)
                run = 1
        changes += run // (k + 1)
        out.append(str(changes))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()