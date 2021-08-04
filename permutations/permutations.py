class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []
        self.solve(nums, permutations, [])
        return permutations
    def solve(self, nums, perms, curr):
        print(f"solve({curr=})")
        current = curr.copy()
        if len(current) == len(nums):
            if current not in perms:
                perms.append(current)
                curr = []
        elif len(curr) == 0:
            for i in range(len(nums)):
                self.solve(nums, perms, [nums[i]])
        else:
            
           # we want to go through all the possible combinations
            # we can start for each index i and append it to the curr
            # and then we can treat the rest of the numbers as a subproblem
            # and append it
            
            for i in range(len(nums)):
                if nums[i] not in current:
                    current.append(nums[i])
                    self.solve(nums, perms, current)
            curr.pop()