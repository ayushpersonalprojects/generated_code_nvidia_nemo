import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    events = []          # (y, delta_width)
    total_area = 0.0
    for _ in range(n):
        # x is irrelevant for horizontal cut
        _ = next(it)      # skip x
        y = float(next(it))
        s = float(next(it))
        if s <= 0:
            continue
        bottom = y
        top = y + s
        width = s
        total_area += s * s
        events.append((bottom, width))
        events.append((top, -width))

    if total_area == 0.0:
        print("0")
        return

    target = total_area / 2.0
    events.sort(key=lambda e: e[0])

    active_width = 0.0
    area_sofar = 0.0
    prev_y = events[0][0] if events else 0.0
    i = 0
    m = len(events)

    while i < m:
        y_curr = events[i][0]
        if y_curr > prev_y:
            seg_h = y_curr - prev_y
            if active_width > 0:
                area_added = active_width * seg_h
                if area_sofar + area_added >= target:
                    needed = target - area_sofar
                    Y = prev_y + needed / active_width
                    print("{:.10f}".format(Y))
                    return
                else:
                    area_sofar += area_added
            else:
                if area_sofar == target:
                    print("{:.10f}".format(prev_y))
                    return
        # apply all events at y_curr
        delta = 0.0
        while i < m and events[i][0] == y_curr:
            delta += events[i][1]
            i += 1
        active_width += delta
        prev_y = y_curr

    # If we reach here, target equals total_area (or zero handled earlier)
    print("{:.10f}".format(prev_y))

if __name__ == "__main__":
    solve()