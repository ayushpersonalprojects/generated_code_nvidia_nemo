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
            water += max(0, left_max - height[left])
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += max(0, right_max - height[right])
    return water

import sys

def main():
    data = sys.stdin.read().strip()
    if not data:
        print(0)
        return
    # Accept numbers separated by any whitespace
    heights = list(map(int, data.split()))
    print(trap_water(heights))

if __name__ == "__main__":
    main()