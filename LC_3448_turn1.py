import sys

def count_substrings(s: str) -> int:
    # cnt[d][r] = number of substrings ending at current position with value % d == r
    # d ranges from 1 to 9
    cnt = [None] + [[0] * d for d in range(1, 10)]
    total = 0
    for ch in s:
        digit = ord(ch) - 48  # faster than int(ch)
        # update counts for each possible divisor d
        for d in range(1, 10):
            prev = cnt[d]
            new = [0] * d
            # extend previous substrings
            for r in range(d):
                c = prev[r]
                if c:
                    nr = (r * 10 + digit) % d
                    new[nr] += c
            # substring consisting of only this digit
            new[digit % d] += 1
            cnt[d] = new
        # if the last digit is not zero, add substrings whose value is divisible by it
        if digit != 0:
            total += cnt[digit][0]
    return total

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    # Detect if first token is number of test cases
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