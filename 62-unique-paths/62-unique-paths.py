class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def printf(nums):
            print("[")
            for i in range(len(nums)):
                print(nums[i])
            print("]")
        dp = []
        for i in range(m):
            dp.append([0] * n)
        
        for i in range(len(dp[0])):
            dp[0][i] = 1
        for i in range (len(dp)):
            dp[i][0] = 1
        for i in range(1,m):
            for j in range (1,n):
                dp[i][j] += (dp[i-1][j])
                dp[i][j] += (dp[i][j-1])
                # printf(dp)
        
        return dp[-1][-1]
    
    