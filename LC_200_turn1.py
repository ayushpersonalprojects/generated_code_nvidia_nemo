import sys

def main():
    data = [line.rstrip('\n') for line in sys.stdin if line.strip() != ""]
    if not data:
        print(0)
        return

    # Determine if first line gives dimensions
    first_tokens = data[0].split()
    if len(first_tokens) == 2 and all(tok.isdigit() for tok in first_tokens):
        n, m = map(int, first_tokens)
        grid = []
        for i in range(1, 1 + n):
            if i >= len(data):
                break
            row = data[i].split()
            # If row tokens are single characters without spaces, treat whole line
            if len(row) == 1 and len(row[0]) == m:
                grid.append(list(row[0]))
            else:
                # Assume each token is a cell (0/1)
                grid.append([int(tok) for tok in row])
        # If fewer rows provided, pad with zeros
        while len(grid) < n:
            grid.append([0] * m)
    else:
        # No dimensions given; infer from lines
        grid = [list(line) for line in data]
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        # Convert characters to int if they are digits
        for i in range(n):
            for j in range(m):
                if grid[i][j].isdigit():
                    grid[i][j] = int(grid[i][j])
                else:
                    # Treat any non-zero char as land
                    grid[i][j] = 1 if grid[i][j] != '0' else 0

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
                stack = [(i, j)]
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if grid[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
    print(count)

if __name__ == "__main__":
    main()