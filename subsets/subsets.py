class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        powerSet = [[]]
        
        for i in range(len(nums)):
            toAdd = nums[i]
            
            for j in range(len(powerSet)):
                powerSet.append(powerSet[j]+[toAdd])
                
        return powerSet