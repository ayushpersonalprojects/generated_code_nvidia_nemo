class Solution:
    def hasMaximalKSubstring(self, s: str, k: int) -> bool:
        """
        Returns True if there exists a substring of length k consisting of identical
        characters that cannot be extended to the left or right while keeping all
        characters identical, and additionally the blocking characters on both sides
        (if they exist) are equal to each other.
        """
        if k <= 0:
            return False
        n = len(s)
        if k > n:
            return False

        i = 0
        while i < n:
            run_char = s[i]
            j = i
            while j < n and s[j] == run_char:
                j += 1
            run_len = j - i
            if run_len == k:
                left = s[i - 1] if i > 0 else None
                right = s[j] if j < n else None
                left_ok = left is None or left != run_char
                right_ok = right is None or right != run_char
                both_exist_and_equal = not (left is not None and right is not None) or left == right
                if left_ok and right_ok and both_exist_and_equal:
                    return True
            i = j
        return False


if __name__ == "__main__":
    sol = Solution()
    assert sol.hasMaximalKSubstring("aaabbcaaa", 3) == True
    assert sol.hasMaximalKSubstring("aaabbcaaa", 2) == False
    assert sol.hasMaximalKSubstring("abcccba", 3) == True
    assert sol.hasMaximalKSubstring("abcccba", 4) == False
    assert sol.hasMaximalKSubstring("a", 1) == True
    assert sol.hasMaximalKSubstring("", 1) == False
    print("All tests passed.")