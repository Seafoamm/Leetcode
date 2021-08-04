class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numDict = {
            "2": ('a', 'b', 'c'),
            "3": ('d', 'e', 'f'),
            "4": ('g', 'h', 'i'),
            "5": ('j', 'k', 'l'),
            "6": ('m', 'n', 'o'),
            "7": ('p', 'q', 'r', 's'),
            "8": ('t', 'u', 'v'),
            "9": ('w', 'x', 'y', 'z')
        }
        if len(digits) == 0:
            return []
        out = [char for char in numDict[digits[0]]]
        out = Solution.generateList(out, digits[1:], numDict)
        
        return out
    
    def generateList(out, digits, numDict):
        # i want to recursively go through each combination possible for phone number letters
        # what do i want to do?
        # for each base (prev string), i want to concatenate each combination of next char
        # dp? build from base up
        # next gen, next gen, etc.
        if not digits:
            return out
        clone = out.copy()
        result = []
        for char in numDict[digits[0]]:
            for ongoing in clone:
                result.append(ongoing + char)
        result = Solution.generateList(result, digits[1:], numDict)
        return result

        
        
        