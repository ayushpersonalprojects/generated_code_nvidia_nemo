def trap_water(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]
    return water

import sys

def main():
    out_lines = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        heights = list(map(int, line.split()))
        out_lines.append(str(trap_water(heights)))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()