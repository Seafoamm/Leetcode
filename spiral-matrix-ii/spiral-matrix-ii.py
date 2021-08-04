class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        nByN = []
        row = [None for i in range(n)]
        for i in range(n):
            nByN.append(row.copy())
        
        UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
        direction = RIGHT
        x, y = 0, 0
        
        for i in range(1, n ** 2 + 1):
            # self.fillMatrixlmao()
            newX, newY = x + direction[0], y + direction[1]
            if not(self.inMatrix(n, newX, newY) and not nByN[newX][newY]):
                if direction == UP:
                    direction = RIGHT
                elif direction == DOWN:
                    direction = LEFT
                elif direction == LEFT:
                    direction = UP
                else:
                    direction = DOWN
                
            nByN[x][y] = i
            x, y = x + direction[0], y + direction[1]
            
            
            
            
        return nByN
    
    def inMatrix(self, n, x, y):
        return x >= 0 and y >= 0 and x < n and y < n