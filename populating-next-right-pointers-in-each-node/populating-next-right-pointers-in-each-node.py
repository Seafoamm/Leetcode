"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        from collections import deque
        queue = deque([root])
        
        while queue:
            length = len(queue)
            # print('queue', end=",")
            # for element in queue:
            #     print(element.val, end='')
            # print()
            for i in range(length):
                curr = queue.popleft()
                # print('queue', end=",")
                # for element in queue:
                #     print(element.val, end='')
                # print()
                if curr.left:
                    queue.append(curr.left)
                    curr.left.next = curr.right
                if curr.right:
                    queue.append(curr.right)
                    if len(queue) > 0 and i != length - 1:
                        # print(f'this={curr.right.val},next={queue[0].left.val}')
                        curr.right.next = queue[0].left

        return root
                
                
#         def dfs(node = root, parent = None):
            
#             if not node:
#                 return
#             # if parent:
#             #     if parent.right:
#             #         node.next = parent.right
            
#             child = node
#             p = parent
#             s = ""
#             if child:
#                 s += str(child.val)
#             else:
#                 s += "None"
#             s += ","
#             if parent:
#                 s += str(parent.val)
#             else:
#                 s += "None"
#             print(s)
#             dfs(node.left, node)
#             dfs(node.right, node)
        
#         dfs()
#         return root

    