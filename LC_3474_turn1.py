def solve() -> None:
    import sys

    data = sys.stdin.read().splitlines()
    if not data:
        return
    # Expect two patterns; ignore extra lines if any
    p1 = data[0].strip()
    p2 = data[1].strip() if len(data) > 1 else ""

    if len(p1) != len(p2):
        print("")
        return

    res_chars = []
    for ch1, ch2 in zip(p1, p2):
        if ch1 != '?' and ch2 != '?' and ch1 != ch2:
            print("")
            return
        if ch1 == '?' and ch2 == '?':
            res_chars.append('a')
        elif ch1 == '?':
            res_chars.append(ch2)
        elif ch2 == '?':
            res_chars.append(ch1)
        else:  # both are same letter
            res_chars.append(ch1)

    print(''.join(res_chars))


if __name__ == "__main__":
    solve()