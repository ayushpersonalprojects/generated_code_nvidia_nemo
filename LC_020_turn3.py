import sys

def main():
    data = sys.stdin.buffer.read()
    # lookup table for ASCII codes: 0 means ignore, otherwise signed value
    tbl = [0] * 256
    tbl[ord('(')] = 1
    tbl[ord('[')] = 2
    tbl[ord('{')] = 3
    tbl[ord(')')] = -1
    tbl[ord(']')] = -2
    tbl[ord('}')] = -3

    stack = []
    for b in data:
        v = tbl[b]
        if v:
            if v > 0:
                stack.append(v)
            else:
                if not stack or stack[-1] != -v:
                    print(False)
                    return
                stack.pop()
    print(not stack)

if __name__ == "__main__":
    main()