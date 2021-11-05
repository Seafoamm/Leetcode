class Solution:
    memo = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        climbStairs = Solution.climbStairs
        memo = Solution.memo
        if memo.get(n, -1) == -1:
            memo[n] = climbStairs(self, n-1) + climbStairs(self, n-2)
            return memo[n]
        else:
            return memo[n]