from collections import deque

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.solve(matrix, 0, len(matrix), 0, len(matrix[0]))
        
         # grab top, rotate to right (save right in temp)
        # use the temp for bottom (save bottom in temp)
        # use bottom for left (save left in temp)
        # use left for top
        # recurse with i - 2 and j - 2 (move in 1 column and move in 1 row, both sides)
        # until you hit length of column and row == 0 (even case), or if column and row == 1, just leave as is (odd case)
    def solve(self, matrix, rowStart, rowEnd, columnStart, columnEnd):
        # print(f"{matrix=}")
        if rowEnd - rowStart < 1:
            return
        elif rowEnd - rowStart == 2:
            topLeft = matrix[rowStart][columnStart]
            topRight = matrix[rowStart][columnEnd - 1]
            bottomLeft = matrix[rowEnd - 1][columnStart]
            bottomRight = matrix[rowEnd - 1][columnEnd - 1]
            
            matrix[rowStart][columnStart] = bottomLeft
            matrix[rowStart][columnEnd - 1] = topLeft
            matrix[rowEnd - 1][columnStart] = bottomRight
            matrix[rowEnd - 1][columnEnd - 1] = topRight
            return
        else:
            top = deque(self.top(matrix, rowStart, rowEnd, columnStart, columnEnd))
            right = deque(self.right(matrix, rowStart, rowEnd, columnStart, columnEnd))
            bottom = deque(self.bottom(matrix, rowStart, rowEnd, columnStart, columnEnd))
            left = deque(self.left(matrix, rowStart, rowEnd, columnStart, columnEnd))
            
            # replace top and bottom
            for i in range(columnStart, columnEnd):
                matrix[rowStart][i] = left.pop()
                matrix[rowEnd - 1][i] = right.pop()
            # replace right and left
            for i in range(rowStart, rowEnd):
                matrix[i][rowStart] = bottom.popleft()
                matrix[i][columnEnd - 1] = top.popleft()
            
            self.solve(matrix, rowStart + 1, rowEnd - 1, columnStart + 1, columnEnd - 1)
    
    def top(self, matrix, rowS, rowE, colS, colE):
        return [matrix[rowS][i] for i in range(colS, colE)]
        
    def right(self, matrix, rowS, rowE, colS, colE):
        return [matrix[i][colE - 1] for i in range(rowS, rowE)]
    
    def bottom(self, matrix, rowS, rowE, colS, colE):
        return [matrix[rowE - 1][i] for i in range(colS, colE)]
    
    def left(self, matrix, rowS, rowE, colS, colE):
        return [matrix[i][colS] for i in range(rowS, rowE)]