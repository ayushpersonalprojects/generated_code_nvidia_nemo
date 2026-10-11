import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # 2n-1 diagonals, indexed by i - j + (n-1)
    diags = [[] for _ in range(2 * n - 1)]
    for i in range(n):
        for j in range(n):
            val = int(next(it))
            diags[i - j + n - 1].append(val)

    # Sort each diagonal increasingly; we'll pop from the end for decreasing order
    for d in diags:
        d.sort()

    out_lines = []
    for i in range(n):
        row_vals = []
        for j in range(n):
            idx = i - j + n - 1
            row_vals.append(str(diags[idx].pop()))  # pop largest remaining
        out_lines.append(' '.join(row_vals))

    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    main()