class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board[0])):
            row = {}
            for j in range(len(board[i])):
                if board[i][j] in row:
                    return False
                else:
                    if board[i][j]!=".":
                        row[board[i][j]] = 1
            col = {}
            for j in range(len(board[i])):
                if board[j][i] in col:
                    return False
                else:
                    if board[j][i]!=".":
                        col[board[j][i]] = 1
            
        li = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]

        for i,j in li:
            group = {}
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if board[k][l] in group:
                        return False
                    else:
                        if board[k][l]!=".":
                            group[board[k][l]] = 1

        return True