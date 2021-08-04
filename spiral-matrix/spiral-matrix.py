class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        NORTH, EAST, SOUTH, WEST = (-1, 0), (0, 1), (1, 0), (0, -1)
        spiral = []
        direction = EAST
        i, j = 0, 0
        visited = {}

        count = 0
        while count < len(matrix) * len(matrix[0]):
            spiral.append(matrix[i][j])
            visited[i, j] = True
            if not self.inMatrix(matrix, i + direction[0], j + direction[1], visited):
                if direction == NORTH:
                    direction = EAST
                elif direction == EAST:
                    direction = SOUTH
                elif direction == SOUTH:
                    direction = WEST
                else:
                    direction = NORTH
            i, j = i + direction[0], j + direction[1]
            count += 1
        
        return spiral
        
        
    
    def inMatrix(self, matrix, i, j, visited):
        return i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[0]) and not visited.get((i, j), False)