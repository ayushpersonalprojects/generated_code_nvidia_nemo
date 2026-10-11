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
        # No explicit basket count; treat remaining as baskets
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
    seg = [-1] * (2 * size)

    # build leaves
    for i in range(n_baskets):
        seg[size + i] = baskets[i]
    for i in range(size - 1, 0, -1):
        seg[i] = max(seg[2 * i], seg[2 * i + 1])

    def update(pos: int, value: int) -> None:
        i = size + pos
        seg[i] = value
        i //= 2
        while i:
            seg[i] = max(seg[2 * i], seg[2 * i + 1])
            i //= 2

    def query_first(node: int, l: int, r: int, fruit: int) -> int:
        if seg[node] < fruit:
            return -1
        if l == r:
            return l
        mid = (l + r) // 2
        left_node = node * 2
        if seg[left_node] >= fruit:
            return query_first(left_node, l, mid, fruit)
        else:
            return query_first(left_node + 1, mid + 1, r, fruit)

    unplaced = 0
    for f in fruits:
        pos = query_first(1, 0, size - 1, f)
        if pos == -1 or pos >= n_baskets:
            unplaced += 1
        else:
            update(pos, -1)  # mark as used

    print(unplaced)


if __name__ == "__main__":
    solve()