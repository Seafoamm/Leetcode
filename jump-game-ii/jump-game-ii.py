class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.solve2(nums)
        # we can go recursive
        # base case: reached the last index
        # else return min of going forward or taking this one
        
    def solve(self, nums, index, jumps):
        if index == len(nums) - 1:
            return jumps
        else:
            stay = float('inf')
            forward = float('inf')
            if index + nums[index] < len(nums):
                stay = self.solve(nums, index + nums[index], jumps + 1)
            if index + 1 < len(nums):
                forward = self.solve(nums, index + 1, jumps + 1)
            return min(stay, forward)
        
    def solve2(self, nums):
        dp = [i for i in range(len(nums))]
        for i in range(len(dp)):
            if i + nums[i] < len(dp):
                for j in range(1, nums[i] + 1):
                    dp[i + j] = min(
                    dp[i + j], dp[i] + 1
                    )
            else:
                dp[-1] = min(
                dp[-1], dp[i] + 1
                )
        
        return dp[-1]