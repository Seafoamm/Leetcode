class Solution:
    def myAtoi(self, s: str) -> int:
        trimmed = s.lstrip()
        if not trimmed:
            return 0
        else:
            num = 0
            negative = trimmed[0] == '-'
            positive = trimmed[0] == '+'
            if negative or positive:
                trimmed = trimmed[1:]
            trimmed = Solution.readTillNextDigit(trimmed)
            if not trimmed:
                return 0
            num = int(trimmed)
            if negative:
                num = num * -1
            if num < -2**31:
                num = -2**31
            elif num > 2**31 - 1:
                num = 2**31 - 1
            return num
            
    def readTillNextDigit(s):
        result = ""
        for char in s:
            if not char.isdigit():
                break
            result = result + char
        
        return result