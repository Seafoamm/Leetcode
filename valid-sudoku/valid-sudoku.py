class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force:
        # make a list of columns
        # check each row for duplicates
        # check each column for duplicates
        # make a list of sub boxes
        # check each sub box for repetition

        
        #optimization: we could check for duplicates as we add in nums
        # we don't even need to make lists of columns/subboxes
        columnList = Solution.listOfColumns(board)
        if not columnList:
            return False

        subBoxList = Solution.listOfSubBoxes(board)
        if not subBoxList:
            return False

        if not Solution.checkRows(board):
            return False

        return True

    def checkRows(board):
        
        for row in board:
            seen = []
            for num in row:
                if num != '.':
                    if num in seen:
                        return False
                    else:
                        seen.append(num)
        return True

    def listOfColumns(board):
        for i in range(9):
            currList = []
            for j in range(9):
                element = board[j][i]
                if element != '.':
                    if element in currList:
                        return False
                    else:
                        currList.append(element)
        return True
    
    def listOfSubBoxes(board):
        ranges = [
            (0, 3, 0, 3),
            (0, 3, 3, 6),
            (0, 3, 6, 9),
            
            (3, 6, 0, 3),
            (3, 6, 3, 6),
            (3, 6, 6, 9),
            
            (6, 9, 0, 3),
            (6, 9, 3, 6),
            (6, 9, 6, 9),
        ]
        
        for (x1, x2, y1, y2) in ranges:
            if not Solution.makeSubBox(board, x1, x2, y1, y2):
                return False
        
        return True
        
    
    def makeSubBox(board, rowStart, rowEnd, colStart, colEnd):
        subBox = []

        for i in range(rowStart, rowEnd):
            for j in range(colStart, colEnd):
                element = board[i][j]
                
                if element != '.':

                    if element in subBox:
                        return False
                    else:
                        subBox.append(board[i][j])
        return True