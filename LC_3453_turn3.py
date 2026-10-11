import sys

def solve():
    data = sys.stdin.buffer.read().split()
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
        total_area = 0       # sum of s*s
        for _ in range(n):
            # x is irrelevant for horizontal cut
            _ = next(it)      # skip x
            y = int(next(it))
            s = int(next(it))
            if s <= 0:
                continue
            bottom = y
            top = y + s
            width = s
            total_area += s * s
            events.append((bottom, width))
            events.append((top, -width))
        if total_area == 0:
            out_lines.append("0")
            continue
        target2 = total_area          # we work with doubled area (half area * 2)
        events.sort(key=lambda e: e[0])
        active = 0                    # current total width
        area2 = 0                     # doubled area accumulated so far
        prev_y = events[0][0] if events else 0
        i = 0
        m = len(events)
        found = False
        while i < m and not found:
            y_curr = events[i][0]
            if y_curr > prev_y:
                seg = y_curr - prev_y
                if active > 0:
                    area2 += active * seg * 2
                    if area2 >= target2:
                        # area before this segment
                        area2_before = area2 - active * seg * 2
                        needed2 = target2 - area2_before   # >=0
                        Y = prev_y + needed2 / (2.0 * active)
                        out_lines.append("{:.10f}".format(Y))
                        found = True
                        break
                else:
                    if area2 == target2:
                        out_lines.append("{:.10f}".format(prev_y))
                        found = True
                        break
            # apply all events at y_curr
            delta = 0
            while i < m and events[i][0] == y_curr:
                delta += events[i][1]
                i += 1
            active += delta
            prev_y = y_curr
        if not found:
            out_lines.append("{:.10f}".format(prev_y))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()