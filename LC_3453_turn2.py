import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    out_lines = []
    while True:
        try:
            n = int(next(it))
        except StopIteration:
            break
        events = []          # (y, delta_width)
        total_area = 0.0
        for _ in range(n):
            # x is irrelevant for horizontal cut
            _ = next(it)      # skip x
            y = float(next(it))
            s = float(next(it))
            if s <= 0.0:
                continue
            bottom = y
            top = y + s
            width = s
            total_area += s * s
            events.append((bottom, width))
            events.append((top, -width))
        if total_area == 0.0:
            out_lines.append("0.0")
            continue
        target = total_area / 2.0
        events.sort(key=lambda e: e[0])
        active_width = 0.0
        area_sofar = 0.0
        prev_y = events[0][0] if events else 0.0
        i = 0
        m = len(events)
        found = False
        while i < m and not found:
            y_curr = events[i][0]
            if y_curr > prev_y:
                seg_h = y_curr - prev_y
                if active_width > 0.0:
                    area_added = active_width * seg_h
                    if area_sofar + area_added >= target:
                        needed = target - area_sofar
                        Y = prev_y + needed / active_width
                        out_lines.append("{:.10f}".format(Y))
                        found = True
                        break
                    else:
                        area_sofar += area_added
                else:
                    if area_sofar == target:
                        out_lines.append("{:.10f}".format(prev_y))
                        found = True
                        break
            # apply all events at y_curr
            delta = 0.0
            while i < m and events[i][0] == y_curr:
                delta += events[i][1]
                i += 1
            active_width += delta
            prev_y = y_curr
        if not found:
            # target equals total_area (should not happen unless total_area==0)
            out_lines.append("{:.10f}".format(prev_y))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()