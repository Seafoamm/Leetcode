class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        from collections import deque
        queue = deque([])
        step = 3
        directions = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0)
            ]
        # find edges
        index = None
        #find initial index
        for i in range(len(grid)):
            found = False
            for j in range(len(grid[0])):
                
                if grid[i][j]:
                    index = i, j
                    found = True
                    break
            
            if found:
                break
        
        def inBounds(move):
            x, y = move
            return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])
        
        def infect(node):
            x, y = node
            for direction in directions:
                nextMove = x + direction[0], y + direction[1]
                x1, y1 = nextMove
                if inBounds(nextMove):
                    if grid[x1][y1] == 1:
                        grid[x1][y1] = 2
                        infect(nextMove)
                    elif grid[x1][y1] == 0:
                        if grid[x][y] != 3:
                            queue.append((x, y))
                            grid[x][y] = 3
                
        infect(index)
        
        
        # bfs
        
        
        while True:
            length = len(queue)

            for i in range(length):
                currEdge = queue.popleft()
                x, y = currEdge
                for direction in directions:
                    nextMove = x + direction[0], y + direction[1]
                    x1, y1 = nextMove
                    if inBounds(nextMove):
                        if grid[x1][y1] == 1:
                            return step - 3
                        elif grid[x1][y1] == 0:
                            grid[x1][y1] = step
                            queue.append((x1, y1))
 
            step += 1
                    
        
        return step - 3
        
        
        '''
        3 1
        3 3
        
        3 2 3 
        3 3 3
        0 3 1
        
        1 1 1 1 1
        1 0 0 0 1
        1 0 1 0 1
        1 0 0 0 1
        1 1 1 1 1
        
        # mark one island as 2s
        # as we mark, grab the edges and put into queue for BFS
        
        
        3 4 4 4 0 0
        2 3 3 4 4 1
        2 3 0 4 0 1
        2 2 2 4 4 1
        4 4 4 4 0 0 
        0 0 0 0 0 0
        
        
        '''