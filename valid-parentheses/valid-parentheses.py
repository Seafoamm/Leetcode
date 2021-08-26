class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        opens = set(['(', '[', '{'])
        closed = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char in opens:
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1] == closed[char]:
                    stack.pop()
                else:
                    return False
        
        
        return not stack