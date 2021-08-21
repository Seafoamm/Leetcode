# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # check if root.left == root.right
        if not root:
            return True
        p = root.left
        q = root.right
        
        
        
        
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
            def recursiveSolution(node1, node2):
                if node1 and not node2:
                    return False
                if node2 and not node1:
                    return False

                if not node1 and not node2:
                    return True

                if node1.val != node2.val:
                    return False


                return recursiveSolution(node1.left, node2.right) and recursiveSolution(node1.right, node2.left)

            pQueue = [p]
            qQueue = [q]

            while pQueue and qQueue:
                p1 = pQueue[0]
                q1 = qQueue[0]

                if p1 and not q1:
                    return False
                if not p1 and q1:
                    return False

                if p1 and q1:
                    if p1.val != q1.val:
                        return False

                del pQueue[0]
                del qQueue[0]

                if p1:
                    pQueue.append(p1.left)
                    pQueue.append(p1.right)
                if q1:
                    qQueue.append(q1.right)
                    qQueue.append(q1.left)


            return not pQueue and not qQueue
        
        return isSameTree(p, q)