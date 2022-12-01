class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        
        ans = 0
        
        
        for i in range(len(matrix)):
            dp[i][0] = 1 if matrix[i][0] == "1" else 0
            ans = max(ans, dp[i][0])
            
        for j in range(len(matrix[0])):
            dp[0][j] = 1 if matrix[0][j] == "1" else 0
            ans = max(ans, dp[0][j])
            
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) if matrix[i][j] == "1" else 0
                ans = max(ans, dp[i][j])
        
        print(dp)
        return ans*ans
        
        