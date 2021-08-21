class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        print(nums)
        solutionSet = []
        
        for i in range(len(nums) - 2):
            if i == 0 or (nums[i] != nums[i-1]):
                low = i + 1
                high = len(nums) - 1
                while low < high:
                    target = -nums[i]
                    lowNum = nums[low]
                    highNum = nums[high]
                    summation = lowNum + highNum
                    if lowNum + highNum == target:
                        solutionSet.append([-target, lowNum, highNum])
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif summation < target:
                        low += 1
                    else:
                        high -= 1
                        
                    
        
        return solutionSet