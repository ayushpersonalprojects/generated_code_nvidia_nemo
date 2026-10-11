import sys

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    idx = 0
    n_fruits = data[idx]
    idx += 1
    fruits = data[idx:idx + n_fruits]
    idx += n_fruits
    if idx >= len(data):
        baskets = data[idx:]
        n_baskets = len(baskets)
    else:
        n_baskets = data[idx]
        idx += 1
        baskets = data[idx:idx + n_baskets]

    if n_baskets == 0:
        print(len(fruits))
        return

    size = 1
    while size < n_baskets:
        size <<= 1
    seg = [0] * (2 * size)

    for i in range(n_baskets):
        seg[size + i] = baskets[i]
    for i in range(size - 1, 0, -1):
        seg[i] = seg[2 * i] if seg[2 * i] >= seg[2 * i + 1] else seg[2 * i + 1]

    def update(pos: int, val: int) -> None:
        i = size + pos
        seg[i] = val
        i //= 2
        while i:
            left = seg[2 * i]
            right = seg[2 * i + 1]
            seg[i] = left if left >= right else right
            i //= 2

    def query_first(fruit: int) -> int:
        if seg[1] < fruit:
            return -1
        i = 1
        while i < size:
            if seg[2 * i] >= fruit:
                i = 2 * i
            else:
                i = 2 * i + 1
        return i - size

    unplaced = 0
    for f in fruits:
        pos = query_first(f)
        if pos == -1 or pos >= n_baskets:
            unplaced += 1
        else:
            update(pos, -1)

    print(unplaced)

if __name__ == "__main__":
    solve()