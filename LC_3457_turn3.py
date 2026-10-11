import sys
import heapq

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    out = []
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
            if d <= 0:
                continue
            pizzas.append((d, v))  # store as (deadline, value)
        # Sort by deadline ascending
        pizzas.sort()
        selected = []  # min-heap of values of chosen pizzas
        for d, v in pizzas:
            if len(selected) < d:
                heapq.heappush(selected, v)
            elif selected[0] < v:
                heapq.heapreplace(selected, v)
        out.append(str(sum(selected)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()