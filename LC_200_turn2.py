import sys
from collections import deque

def main():
    data = [line.rstrip('\n') for line in sys.stdin if line.strip() != ""]
    if not data:
        print(0)
        return

    # Detect if first line gives dimensions
    first = data[0].split()
    if len(first) == 2 and all(tok.isdigit() for tok in first):
        n, m = map(int, first)
        grid = []
        idx = 1
        for _ in range(n):
            if idx >= len(data):
                row = []
            else:
                line = data[idx]
                idx += 1
                if ' ' in line:
                    parts = line.split()
                    row = [int(p) for p in parts]
                else:
                    row = [1 if ch != '0' else 0 for ch in line]
            # Ensure row length m
            if len(row) < m:
                row += [0] * (m - len(row))
            elif len(row) > m:
                row = row[:m]
            grid.append(row)
    else:
        # No dimensions given
        grid = []
        for line in data:
            if ' ' in line:
                parts = line.split()
                row = [int(p) for p in parts]
            else:
                row = [1 if ch != '0' else 0 for ch in line]
            grid.append(row)
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0

    if n == 0 or m == 0:
        print(0)
        return

    visited = [[False] * m for _ in range(n)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    count = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                count += 1
                dq = deque()
                dq.append((i, j))
                visited[i][j] = True
                while dq:
                    x, y = dq.popleft()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if grid[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                dq.append((nx, ny))
    print(count)

if __name__ == "__main__":
    main()