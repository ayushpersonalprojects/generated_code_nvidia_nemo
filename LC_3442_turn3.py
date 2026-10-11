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
    has_odd = has_even = False

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
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    first = data[0]
    # Try to interpret first token as number of test cases
    if first.isdigit():
        t = int(first)
        if len(data) == t + 1:
            out = []
            idx = 1
            for _ in range(t):
                s = data[idx].decode()
                idx += 1
                out.append(str(process_string(s)))
            sys.stdout.write("\n".join(out))
            return

    # Otherwise treat every token as a separate test case
    out = []
    for token in data:
        s = token.decode()
        out.append(str(process_string(s)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()