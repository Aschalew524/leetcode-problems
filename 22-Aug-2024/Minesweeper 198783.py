# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        visited = set()
        direction = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        
        def dfs(row, col):
            if not inbound(row, col) or (row, col) in visited:
                return
            
            visited.add((row, col))
            
            if board[row][col] == "M":
                board[row][col] = "X"
            elif board[row][col] == "E":
                count = 0
                for x, y in direction:
                    new_row, new_col = row + x, col + y
                    if inbound(new_row, new_col) and board[new_row][new_col] == "M":
                        count += 1
                
                if count > 0:
                    board[row][col] = str(count)
                else:
                    board[row][col] = "B"
                    for x, y in direction:
                        new_row, new_col = row + x, col + y
                        dfs(new_row, new_col)
        
        dfs(click[0], click[1])
        return board