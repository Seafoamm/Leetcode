class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indexMap = {}
        
        for i in range(len(nums)):
            difference = target - nums[i]
            
            if difference in indexMap:
                return [indexMap[difference], i]
            else:
                indexMap[nums[i]] = i
        
 