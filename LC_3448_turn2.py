import sys

def build_transition():
    trans = [None] * 10  # index by d (1..9)
    for d in range(1, 10):
        table = [[0] * 10 for _ in range(d)]
        for r in range(d):
            for dig in range(10):
                table[r][dig] = (r * 10 + dig) % d
        trans[d] = table
    return trans

TRANS = build_transition()

def count_substrings(s: str) -> int:
    # cnt[d][r] = number of substrings ending at current position with value % d == r
    cnt = [None] + [[0] * d for d in range(1, 10)]
    total = 0
    for ch in s:
        digit = ord(ch) - 48  # faster than int(ch)
        # update counts for each divisor d
        for d in range(1, 10):
            prev = cnt[d]
            new = [0] * d
            tr = TRANS[d]
            # extend previous substrings
            for r in range(d):
                c = prev[r]
                if c:
                    new[tr[r][digit]] += c
            # substring consisting of only this digit
            new[digit % d] += 1
            cnt[d] = new
        if digit != 0:
            total += cnt[digit][0]
    return total

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    if len(data) > 1 and data[0].isdigit() and len(data[0]) <= 6:
        t = int(data[0])
        idx = 1
        out_lines = []
        for _ in range(t):
            if idx >= len(data):
                s = ''
            else:
                s = data[idx]
                idx += 1
            out_lines.append(str(count_substrings(s)))
        sys.stdout.write("\n".join(out_lines))
    else:
        s = data[0]
        sys.stdout.write(str(count_substrings(s)))

if __name__ == "__main__":
    solve()