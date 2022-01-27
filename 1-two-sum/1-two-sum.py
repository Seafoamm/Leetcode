class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # goal: linear time
        # 2nd goal: 1 pass
        
        # 1. go through each numebr
        # 2. subtract from target and put in set
        # 3. we need to return the indices ???
        # 4. because we lose the index when we put it into the set
        
        # 5. SOOO there are 2 solutions:
        # 6. store tuples in the set
        # 7. map
        num_dict = {}
        
        for i in range(len(nums)):
            curr = nums[i]
            if curr in num_dict:
                return [i, num_dict[curr]]
            else:
                num_dict[target - curr] = i
                
                
        return []
        