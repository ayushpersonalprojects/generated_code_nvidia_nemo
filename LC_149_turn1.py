def max_points_on_line(points):
    """
    Returns the maximum number of points that lie on the same straight line.
    :param points: List of [x, y] coordinates (list of lists or tuples)
    :return: Integer representing the max number of collinear points
    """
    if not points:
        return 0
    n = len(points)
    if n <= 2:
        return n

    from math import gcd
    best = 0

    for i in range(n):
        slopes = {}
        duplicate = 0
        xi, yi = points[i]

        for j in range(i + 1, n):
            xj, yj = points[j]
            dx = xj - xi
            dy = yj - yi

            if dx == 0 and dy == 0:
                duplicate += 1
                continue

            g = gcd(dx, dy)
            dx //= g
            dy //= g

            # Normalize direction to have a unique representation
            if dx < 0:
                dx, dy = -dx, -dy
            elif dx == 0:
                if dy < 0:
                    dy = -dy
            # else dx > 0, keep as is

            slopes[(dx, dy)] = slopes.get((dx, dy), 0) + 1

        # At least the point itself plus any duplicates
        cur_max = duplicate + 1
        for count in slopes.values():
            cur_max = max(cur_max, count + duplicate + 1)

        best = max(best, cur_max)

    return best