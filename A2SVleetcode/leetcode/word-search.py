class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def b_track(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[i] or
                    (r, c) in visited):
                return False

            visited.add((r, c))
            found = (b_track(r + 1, c, i + 1) or
                     b_track(r - 1, c, i + 1) or
                     b_track(r, c + 1, i + 1) or
                     b_track(r, c - 1, i + 1))

            visited.remove((r, c))  
            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                if b_track(r, c, 0):
                    return True
        return False
