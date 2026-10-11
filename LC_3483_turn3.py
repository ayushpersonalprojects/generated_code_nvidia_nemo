import sys

def count_line(s: str) -> int:
    freq = [0] * 10
    for ch in s:
        if '0' <= ch <= '9':
            freq[ord(ch) - 48] += 1

    total = 0
    for h in range(1, 10):          # hundreds digit (cannot be 0)
        if freq[h] == 0:
            continue
        freq[h] -= 1
        for t in range(10):         # tens digit
            if freq[t] == 0:
                continue
            freq[t] -= 1
            for u in (0, 2, 4, 6, 8):  # units digit must be even
                if freq[u] > 0:
                    total += 1
            freq[t] += 1
        freq[h] += 1
    return total

def main():
    out_lines = []
    for line in sys.stdin:
        line = line.rstrip('\n')
        out_lines.append(str(count_line(line)))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()