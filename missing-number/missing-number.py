class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summation = sum(range(len(nums)+1))
        
        return summation - sum(nums)