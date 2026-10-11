import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    try:
        N = int(next(it))
        M = int(next(it))
    except StopIteration:
        return
    pizzas = []
    for _ in range(M):
        d = int(next(it))
        v = int(next(it))
        if d > N:
            d = N
        if d < 1:
            continue
        pizzas.append((v, d))
    # Sort by value descending
    pizzas.sort(reverse=True)
    parent = list(range(N + 2))  # 0..N+1

    def find(x):
        # Path compression
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        xr = find(x)
        yr = find(y)
        if xr != yr:
            parent[xr] = yr

    total = 0
    for v, d in pizzas:
        avail = find(d)
        if avail > 0:
            total += v
            union(avail, avail - 1)
    print(total)

if __name__ == "__main__":
    solve()