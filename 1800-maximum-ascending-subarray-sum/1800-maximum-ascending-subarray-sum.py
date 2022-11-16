class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxSum = nums[0]
        currSum = nums[0]
        prev = nums[0]
        
        for i in range(1, len(nums)):
            currNum = nums[i]
            if currNum <= prev:
                currSum = currNum
            else:
                currSum += currNum
            prev = currNum
            maxSum = max(currSum, maxSum)

            
        return maxSum