class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        def dfs(i, j, c = 0):
            if c == len(word):
                return True
            if i < 0 or j < 0 or i>= n or j >= m or board[i][j] != word[c]:
                return False
            temp = board[i][j]
            board[i][j] = '.'
            if dfs(i+1, j, c+1):
                return True
            if dfs(i-1, j, c+1):
                return True
            if dfs(i, j+1, c+1):
                return True
            if dfs(i, j-1, c+1):
                return True
            board[i][j] = temp
            return False
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j):
                        return True
        return False