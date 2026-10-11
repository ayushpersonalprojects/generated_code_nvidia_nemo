import sys
from collections import defaultdict

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # Read matrix
    matrix = [[int(next(it)) for _ in range(n)] for __ in range(n)]

    # Gather elements of each diagonal (identified by i - j)
    diags = defaultdict(list)
    for i in range(n):
        for j in range(n):
            diags[i - j].append(matrix[i][j])

    # Sort each diagonal in ascending order; we'll pop from the end for descending
    for k in diags:
        diags[k].sort()

    # Reconstruct matrix with diagonals sorted in non‑increasing order
    out_lines = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(str(diags[i - j].pop()))  # pop largest remaining
        out_lines.append(' '.join(row))

    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    main()