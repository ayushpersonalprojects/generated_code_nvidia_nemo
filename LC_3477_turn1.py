import sys

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    idx = 0
    n = data[idx]
    idx += 1
    fruits = data[idx:idx + n]
    idx += n
    if idx >= len(data):
        # No basket count provided; assume remaining are basket capacities
        baskets = data[idx:]
        m = len(baskets)
    else:
        m = data[idx]
        idx += 1
        baskets = data[idx:idx + m]
    used = [False] * m
    unplaced = 0
    for f in fruits:
        placed = False
        for i in range(m):
            if not used[i] and baskets[i] >= f:
                used[i] = True
                placed = True
                break
        if not placed:
            unplaced += 1
    print(unplaced)

if __name__ == "__main__":
    solve()