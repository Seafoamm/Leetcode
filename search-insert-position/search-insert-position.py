class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        while(end >= start):
            
            if nums[mid] == target:
                return mid
            else:
                if target < nums[mid]:
                    end = mid - 1
                    mid = (start + end) // 2
                elif target > nums[mid]:
                    start = mid + 1
                    mid = (start + end) // 2
            
                    
        return start