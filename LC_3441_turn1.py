import sys

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    # Try to parse N, K, S from the input.
    # Expected format: N K on first line, S on second line.
    # Fallbacks are provided for common variations.
    try:
        N = int(data[0])
        K = int(data[1])
        S = data[2] if len(data) > 2 else ''
    except ValueError:
        # Maybe the order is N, S, K
        try:
            N = int(data[0])
            S = data[1]
            K = int(data[2]) if len(data) > 2 else 0
        except ValueError:
            # Last resort: treat the first token as the string,
            # compute its length, and assume K = 1.
            S = data[0]
            N = len(S)
            K = 1

    # If the provided length does not match the actual string, adjust.
    if len(S) != N:
        N = len(S)

    ans = 0
    i = 0
    while i < N:
        j = i
        while j < N and S[j] == S[i]:
            j += 1
        run_len = j - i
        ans += run_len // (K + 1)
        i = j

    print(ans)


if __name__ == "__main__":
    solve()