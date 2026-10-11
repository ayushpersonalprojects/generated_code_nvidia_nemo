def solve() -> None:
    import sys

    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    # Take the first two lines as the patterns (ignore any extra lines)
    p1 = lines[0].strip()
    p2 = lines[1].strip() if len(lines) > 1 else ""

    if len(p1) != len(p2):
        print("")
        return

    result = []
    for ch1, ch2 in zip(p1, p2):
        if ch1 != '?' and ch2 != '?' and ch1 != ch2:
            print("")
            return
        if ch1 == '?' and ch2 == '?':
            result.append('a')
        elif ch1 == '?':
            result.append(ch2)
        elif ch2 == '?':
            result.append(ch1)
        else:  # both are the same letter
            result.append(ch1)

    print(''.join(result))


if __name__ == "__main__":
    solve()