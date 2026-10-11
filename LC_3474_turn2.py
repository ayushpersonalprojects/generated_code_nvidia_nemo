def solve() -> None:
    import sys

    tokens = sys.stdin.read().split()
    if not tokens:
        return

    # Helper to process a single pair of patterns
    def process(p1: str, p2: str) -> str:
        if len(p1) != len(p2):
            return ""
        res = []
        for a, b in zip(p1, p2):
            if a != '?' and b != '?' and a != b:
                return ""
            if a == '?' and b == '?':
                res.append('a')
            elif a == '?':
                res.append(b)
            elif b == '?':
                res.append(a)
            else:  # both are same letter
                res.append(a)
        return ''.join(res)

    # If the first token is an integer and matches the expected number of remaining tokens,
    # treat it as the number of test cases.
    if tokens[0].isdigit():
        t = int(tokens[0])
        expected = 1 + 2 * t
        if len(tokens) != expected:
            # malformed input; fallback to single case handling
            p1 = tokens[0] if len(tokens) > 0 else ""
            p2 = tokens[1] if len(tokens) > 1 else ""
            sys.stdout.write(process(p1, p2))
            return
        idx = 1
        out = []
        for _ in range(t):
            p1 = tokens[idx]
            p2 = tokens[idx + 1]
            idx += 2
            out.append(process(p1, p2))
        sys.stdout.write("\n".join(out))
    else:
        # Single test case: first two tokens are the patterns
        p1 = tokens[0] if len(tokens) > 0 else ""
        p2 = tokens[1] if len(tokens) > 1 else ""
        sys.stdout.write(process(p1, p2))


if __name__ == "__main__":
    solve()