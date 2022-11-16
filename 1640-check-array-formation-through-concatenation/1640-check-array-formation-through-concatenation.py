class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dict = {}
            
        for piece in pieces:
            dict[piece[0]] = piece
        
        i = 0
        
        while i < len(arr):
            currNum = arr[i]
            j = 0
            if currNum not in dict:
                return False
            while j < len(dict[currNum]):
                if arr[i] != dict[currNum][j]:
                    return False
                i += 1
                j += 1
        
        
        return True
            
        