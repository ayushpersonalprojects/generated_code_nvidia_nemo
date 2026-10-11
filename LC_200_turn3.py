import sys
from collections import deque

def main():
    data = [line.rstrip('\n') for line in sys.stdin if line.strip() != ""]
    if not data:
        print(0)
        return

    first = data[0].split()
    if len(first) == 2 and all(tok.isdigit() for tok in first):
        n, m = map(int, first)
        grid = []
        idx = 1
        for _ in range(n):
            if idx >= len(data):
                row = [0] * m
            else:
                line = data[idx]
                idx += 1
                if ' ' in line:
                    parts = line.split()
                    row = [int(p) for p in parts]
                else:
                    row = [1 if ch != '0' else 0 for ch in line]
            if len(row) < m:
                row += [0] * (m - len(row))
            elif len(row) > m:
                row = row[:m]
            grid.append(row)
    else:
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

    count = 0
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                count += 1
                dq = deque()
                dq.append((i, j))
                grid[i][j] = 0
                while dq:
                    x, y = dq.popleft()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                            dq.append((nx, ny))
    print(count)

if __name__ == "__main__":
    main()