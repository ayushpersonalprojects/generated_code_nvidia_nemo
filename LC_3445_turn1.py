import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    s = data[0].strip()
    L = int(data[1]) if len(data) > 1 else 0
    n = len(s)
    if L <= 0 or L > n:
        print(0)
        return

    # Assume input consists of lowercase English letters.
    prefix = [0] * (n + 1)
    for i, ch in enumerate(s, 1):
        bit = 1 << (ord(ch) - 97)
        prefix[i] = prefix[i - 1] ^ bit

    seen = []
    max_odd = 0
    full_mask = (1 << 26) - 1  # not used directly, just for clarity

    for i in range(L, n + 1):
        # make prefix[i-L] available as a left boundary
        seen.append(prefix[i - L])
        cur = prefix[i]
        for mask in seen:
            odd = (cur ^ mask).bit_count()
            if odd > max_odd:
                max_odd = odd
                if max_odd == 26:   # cannot exceed alphabet size
                    break
        if max_odd == 26:
            break

    diff = 2 * max_odd - 26
    print(diff)

if __name__ == "__main__":
    main()