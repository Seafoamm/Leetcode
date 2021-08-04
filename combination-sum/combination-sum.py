class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        self.solve(candidates, target, combinations, [])
        return combinations
        
        # keep adding numbers starting from the beginning
        # recursively trying numbers
        
    def solve(self, candidates, target, combinations, currList):
        if sum(currList) == target:
            curr = sorted(currList)
            if curr not in combinations:
                combinations.append(curr)
            currList.pop()
            return
        elif sum(currList) > target:
            currList.pop()
            return
        else:
            for i in range(len(candidates)):
                currList.append(candidates[i])
                self.solve(candidates, target, combinations, currList)
            if currList:
                    currList.pop()