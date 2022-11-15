class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            current = nums[i]
            complement = target - current
            if complement in dict:
                return [i, dict[complement]]
            else:
                dict[nums[i]] = i
            
            