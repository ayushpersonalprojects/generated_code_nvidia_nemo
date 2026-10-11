import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    out_lines = []
    while True:
        try:
            N = int(next(it))
            M = int(next(it))
        except StopIteration:
            break
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
        parent = {}

        def find(x):
            # Find the greatest available day <= x
            orig = x
            while x in parent:
                x = parent[x]
            # Path compression
            while orig in parent:
                nxt = parent[orig]
                parent[orig] = x
                orig = nxt
            return x

        total = 0
        for v, d in pizzas:
            avail = find(d)
            if avail > 0:
                total += v
                parent[avail] = find(avail - 1)
        out_lines.append(str(total))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()