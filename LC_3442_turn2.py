import sys

def process_string(s: str) -> int:
    if not s:
        return 0
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    max_odd = -1
    min_odd = 10**9
    max_even = -1
    min_even = 10**9
    has_odd = False
    has_even = False

    for v in freq.values():
        if v & 1:          # odd
            has_odd = True
            if v > max_odd:
                max_odd = v
            if v < min_odd:
                min_odd = v
        else:              # even
            has_even = True
            if v > max_even:
                max_even = v
            if v < min_even:
                min_even = v

    if not has_odd or not has_even:
        return 0
    return max(max_odd - min_even, max_even - min_odd)


def solve() -> None:
    data = sys.stdin.read().splitlines()
    if not data:
        return

    # Try to interpret first line as number of test cases
    try:
        t = int(data[0].strip())
        idx = 1
        out = []
        for _ in range(t):
            s = data[idx].rstrip('\n') if idx < len(data) else ''
            idx += 1
            out.append(str(process_string(s)))
        sys.stdout.write("\n".join(out))
    except ValueError:
        # No test case count; treat each line as a separate test case
        out = []
        for line in data:
            s = line.strip()
            if s == '':
                continue
            out.append(str(process_string(s)))
        sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()