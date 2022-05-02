class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        
        dp = []
        for i in range(m):
            dp.append([0] * n)
        
        for i in range(len(dp[0])):
            dp[0][i] = 1
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
                break
        for i in range (len(dp)):
            dp[i][0] = 1
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                break
                
                
        for i in range(1,m):
            for j in range (1,n):
                dp[i][j] += (dp[i-1][j])
                dp[i][j] += (dp[i][j-1])
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                # printf(dp)
        
        return dp[-1][-1]
    