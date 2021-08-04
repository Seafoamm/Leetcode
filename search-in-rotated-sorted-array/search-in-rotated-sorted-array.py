class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # why don't we just do a binary search of both halves
        
        if len(nums) == 2:
            ans = -1
            if target == nums[0]:
                ans = 0
            if target == nums[1]:
                ans = 1
            return ans
        
        start1 = 0
        end1 = 0
        start2 = 0
        end2 = 0
        rotated = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                end1 = i - 1
                start2 = i
                end2 = len(nums) - 1
                rotated = True
                break
        
        if not end1:
            if rotated:
                ans = 0 if nums[0] == target else -1
            else:
                ans = Solution.binarySearch(nums, target, 0, len(nums) - 1)
        else:
            ans = Solution.binarySearch(nums, target, start1, end1)    
        
        if ans == -1:
            ans = Solution.binarySearch(nums, target, start2, end2)
        return ans
    
    def binarySearch(nums, target, s, e):
        start = s
        end = e
        mid = (start + end) // 2
        while end >= start:
            look = nums[mid]
            if look == target:
                return mid
            elif look < target:
                start = mid + 1
            elif look > target:
                end = mid - 1
            mid = (start + end) // 2
        
        return -1