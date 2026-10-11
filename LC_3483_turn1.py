import sys
from collections import Counter

def main():
    data = sys.stdin.read()
    digits = [ch for ch in data if ch.isdigit()]
    supply = Counter(digits)

    count = 0
    for num in range(100, 1000, 2):  # three-digit even numbers
        needed = Counter(str(num))
        if all(needed[d] <= supply.get(d, 0) for d in needed):
            count += 1
    print(count)

if __name__ == "__main__":
    main()