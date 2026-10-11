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
    return not stack

def main():
    # Read the entire input as a single string (ignore trailing newlines)
    data = sys.stdin.read()
    s = data.rstrip('\n')
    print(is_balanced(s))

if __name__ == "__main__":
    main()