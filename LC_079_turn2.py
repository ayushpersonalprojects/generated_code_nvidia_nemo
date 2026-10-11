class Solution:
    def exist(self, board, word):
        """
        Returns True if the word can be found in the board by moving
        horizontally or vertically to adjacent cells without reusing a cell.
        """
        if not board or not board[0]:
            return not word
        if not word:
            return True

        rows, cols = len(board), len(board[0])
        L = len(word)

        def dfs(r, c, idx):
            # All characters matched
            if idx == L:
                return True
            # Out of bounds or mismatch
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[idx]:
                return False

            # Mark the cell as visited
            temp = board[r][c]
            board[r][c] = None  # sentinel that won't match any letter

            # Explore the four neighbours
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if dfs(r + dr, c + dc, idx + 1):
                    board[r][c] = temp   # restore before returning
                    return True

            # Backtrack
            board[r][c] = temp
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False