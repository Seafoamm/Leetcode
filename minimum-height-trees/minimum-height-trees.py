class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # build all combinations of trees using recursive backtracking
        # visited array - to keep track of if we have completed a tree (if not all visited, tree is not completed yet)
        # dictionary to map each root to its minimum height
        # recursive backtracking to find the minimum trees

        if n == 0:
            return []
        elif n == 1:
            return [0]
        
        adj = {i: [] for i in range(n)}
        degrees = {i: 0 for i in range(n)}
        
        for edge in edges:
            first = edge[0]
            second = edge[1]
            
            adj[first].append(second)
            adj[second].append(first)
            
            degrees[first] += 1
            degrees[second] += 1
        
        from collections import deque
        
        queue = deque()
        for i in degrees:
            if degrees[i] == 1:
                queue.append(i)
                
        nodesLeft = n
        
        while nodesLeft > 2:
            length = len(queue)
            nodesLeft -= length
            
            while length > 0:
                currentNode = queue.popleft()
                degrees[currentNode] -= 1
                for neighbor in adj[currentNode]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        queue.append(neighbor)
                
                length -= 1
        
        return list(queue)