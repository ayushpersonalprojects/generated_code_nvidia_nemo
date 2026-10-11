import sys

def is_balanced(s: str) -> bool:
    stack = []
    opening = {'(', '[', '{'}
    matching = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in opening:
            stack.append(ch)
        elif ch in matching:
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()
        # ignore any other characters
    return not stack

def main():
    data = sys.stdin.read()
    # Remove trailing newlines but keep possible internal spaces as part of the string
    s = data.strip('\n')
    print(is_balanced(s))

if __name__ == "__main__":
    main()