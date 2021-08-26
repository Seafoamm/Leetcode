class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        minSum = 0
        
        if not grid:
            return 0
        
        
        dp = []
        for i in range(len(grid)):
            dp.append([float('inf')] * len(grid[0]))
        
        dp[0][0] = grid[0][0]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i + 1 < len(dp):
                    dp[i+1][j] = min(dp[i+1][j], dp[i][j]+grid[i+1][j])
                if j + 1 < len(dp[0]):
                    dp[i][j+1] = min(dp[i][j+1], dp[i][j]+grid[i][j+1])
                    
        return dp[-1][-1]
                