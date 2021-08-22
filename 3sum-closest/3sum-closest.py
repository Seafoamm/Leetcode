class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = None
        nums.sort()
        for i in range(len(nums) - 2):
            current = nums[i]
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                lNum = nums[left]
                rNum = nums[right]
                summation = current + lNum + rNum
                # print(i, left, right)
                # print(summation)
                if closest == None or abs(summation - target) < abs(closest - target):
                    closest = summation
                
                if summation == target:
                    return summation
                
                if summation < target:
                    left += 1
                elif summation > target:
                    right -= 1
                
                
                
        return closest