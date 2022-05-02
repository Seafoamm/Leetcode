class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRows = set()
        zeroColumns = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroColumns.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i in zeroRows) or (j in zeroColumns):
                    matrix[i][j] = 0
                    
        