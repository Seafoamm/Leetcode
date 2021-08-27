class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        A B C E
        S F E S
        A D E E
        (0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (1, 2), (1, 1), (1, 0)
        '''
        visited = set()
        def dfs(i, j, index = 0):

            if index == len(word):
                return True
            
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:

                return False
            
            if (i, j) in visited:

                return False
            else:
                visited.add((i, j))
                
            
            
            if board[i][j] == word[index]:
                index += 1
                ans = dfs(i+1, j, index) or dfs(i-1, j, index) or dfs(i, j+1, index) or dfs(i, j-1, index)
                visited.remove((i, j))
                return ans
            else:
                visited.remove((i, j))

                return False
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
                    
                    # visited = set()
        
        return False
                    