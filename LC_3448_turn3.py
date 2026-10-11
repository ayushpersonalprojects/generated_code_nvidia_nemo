import sys

# Precompute transition tables: trans[d][r][digit] = (r*10+digit) % d
TRANS = [[[0] * 10 for _ in range(d)] for d in range(10)]  # index by d (0..9), we use 1..9
for d in range(1, 10):
    td = TRANS[d]
    for r in range(d):
        row = td[r]
        for dig in range(10):
            row[dig] = (r * 10 + dig) % d

def count_substrings(s: str) -> int:
    # Convert characters to ints once
    digits = [ord(c) - 48 for c in s]
    # cnt[d][r] for d=1..9
    cnt = [None] + [[0] * d for d in range(1, 10)]
    total = 0
    for dig in digits:
        # update counts for each divisor d
        for d in range(1, 10):
            prev = cnt[d]
            new = [0] * d
            tr = TRANS[d]
            # extend previous substrings
            for r in range(d):
                c = prev[r]
                if c:
                    new[tr[r][dig]] += c
            # substring consisting of only this digit
            new[dig % d] += 1
            cnt[d] = new
        if dig != 0:
            total += cnt[dig][0]
    return total

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    if len(data) > 1 and data[0].isdigit() and len(data[0]) <= 6:
        t = int(data[0])
        idx = 1
        out = []
        for _ in range(t):
            if idx >= len(data):
                s = ''
            else:
                s = data[idx]
                idx += 1
            out.append(str(count_substrings(s)))
        sys.stdout.write("\n".join(out))
    else:
        s = data[0]
        sys.stdout.write(str(count_substrings(s)))

if __name__ == "__main__":
    solve()