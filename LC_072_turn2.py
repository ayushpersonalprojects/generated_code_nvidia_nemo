class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Compute the Levenshtein distance between two strings.
        Returns the minimum number of insertions, deletions, or substitutions
        required to transform word1 into word2.
        """
        if len(word1) < len(word2):
            word1, word2 = word2, word1  # ensure word1 is the longer string for space optimization

        previous = list(range(len(word2) + 1))
        for i, c1 in enumerate(word1, 1):
            current = [i] + [0] * len(word2)
            for j, c2 in enumerate(word2, 1):
                insert_cost = current[j - 1] + 1
                delete_cost = previous[j] + 1
                replace_cost = previous[j - 1] + (c1 != c2)
                current[j] = min(insert_cost, delete_cost, replace_cost)
            previous = current
        return previous[-1]