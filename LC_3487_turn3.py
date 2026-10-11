def solve():
    import sys
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    nums = list(map(int, data))

    # Try to interpret first number as number of test cases
    T = nums[0]
    ptr = 1
    answers = []
    ok = True
    for _ in range(T):
        if ptr >= len(nums):
            ok = False
            break
        n = nums[ptr]
        ptr += 1
        if ptr + n > len(nums):
            ok = False
            break
        seen = set()
        total = 0
        for i in range(ptr, ptr + n):
            x = nums[i]
            if x > 0 and x not in seen:
                seen.add(x)
                total += x
        answers.append(total)
        ptr += n
    if ok and ptr == len(nums):
        sys.stdout.write("\n".join(map(str, answers)))
        return

    # Fallback: treat input as a single test case with leading n
    ptr = 0
    if ptr < len(nums):
        n = nums[ptr]
        ptr += 1
        if ptr + n <= len(nums):
            arr = nums[ptr:ptr + n]
            seen = set()
            total = 0
            for x in arr:
                if x > 0 and x not in seen:
                    seen.add(x)
                    total += x
            sys.stdout.write(str(total))
            return

    # Fallback: treat all numbers as the array (no explicit n)
    seen = set()
    total = 0
    for x in nums:
        if x > 0 and x not in seen:
            seen.add(x)
            total += x
    sys.stdout.write(str(total))

if __name__ == "__main__":
    solve()