import sys

def count_for_line(line: str) -> int:
    freq = [0] * 10
    for ch in line:
        if ch.isdigit():
            freq[ord(ch) - 48] += 1

    total = 0
    for h in range(1, 10):          # hundreds digit cannot be 0
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
    lines = sys.stdin.read().splitlines()
    results = []
    for line in lines:
        if line.strip() == "":
            continue
        results.append(str(count_for_line(line)))
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()