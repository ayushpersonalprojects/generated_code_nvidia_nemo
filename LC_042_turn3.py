def trap_water(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = height[left]
    right_max = height[right]
    water = 0
    while left < right:
        if left_max < right_max:
            left += 1
            if height[left] > left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
        else:
            right -= 1
            if height[right] > right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
    return water

import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    nums = list(map(int, data))
    # If first number looks like a length prefix, skip it
    if len(nums) >= 2 and nums[0] == len(nums) - 1:
        heights = nums[1:]
    else:
        heights = nums
    sys.stdout.write(str(trap_water(heights)))

if __name__ == "__main__":
    main()