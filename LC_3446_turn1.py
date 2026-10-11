import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    vals = list(map(int, data[1:]))
    # Build matrix
    matrix = []
    idx = 0
    for _ in range(n):
        row = vals[idx:idx + n]
        matrix.append(row)
        idx += n

    # Sort each top-left to bottom-right diagonal in non-increasing order
    # Diagonals starting from the first row
    for start_col in range(n):
        i, j = 0, start_col
        diag = []
        while i < n and j < n:
            diag.append(matrix[i][j])
            i += 1
            j += 1
        diag.sort(reverse=True)
        i, j = 0, start_col
        for val in diag:
            matrix[i][j] = val
            i += 1
            j += 1

    # Diagonals starting from the first column (excluding the (0,0) diagonal already handled)
    for start_row in range(1, n):
        i, j = start_row, 0
        diag = []
        while i < n and j < n:
            diag.append(matrix[i][j])
            i += 1
            j += 1
        diag.sort(reverse=True)
        i, j = start_row, 0
        for val in diag:
            matrix[i][j] = val
            i += 1
            j += 1

    # Output the resulting matrix
    out = '\n'.join(' '.join(map(str, row)) for row in matrix)
    sys.stdout.write(out)

if __name__ == "__main__":
    main()