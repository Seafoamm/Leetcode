class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        # first instinct: we can grab the starting edge (maybe we have to find the starting edge? any edge that has the start node as the first element)
        # then we can go to any other node that has the 2nd element in your starting edge
        # etc until you hit the end (with backtracking)
        
        
        # ideas:
        # bfs?
        # indegrees/outdegrees (can make adjacency list)
        if start == end:
            return True
        
        from collections import deque
        
        queue = deque()
        
        adj = {i: [] for i in range(n)}
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        visited = {key: False for key in adj}
        
        queue.append(start)
        
        while queue:
            curr = queue.popleft()
            visited[curr] = True
            if curr == end:
                return True
            for node in adj[curr]:
                if not visited[node]:
                    queue.append(node)
        
        
        return False