class Solution:
    def countAndSay(self, n: int) -> str:
        return self.solve("", 1, n)
        
    def solve(self, stringNum, start, n):
        if start > n:
            return stringNum
        else:
            if start == 1: 
                return self.solve(stringNum + '1', start + 1, n)
            else:
                groups = []
                self.partitionNumber(stringNum, groups)
                return self.solve(self.convert(groups), start + 1, n)
        
        
    def partitionNumber(self, stringNum, groups):
        current = stringNum[0]
        currList = []
        for char in stringNum:
            if char == current:
                currList.append(char)
            else:
                current = char
                groups.append(currList)
                currList = []
                currList.append(current)
        groups.append(currList)
        
    def convert(self, groups):
        conversion = ""
        for group in groups:
            conversion += str(len(group)) + group[0]
        return conversion