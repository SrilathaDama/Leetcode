# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        q = [root]

        while q:
            l = len(q)
            for i, n in enumerate(q):
                if n != u:
                    continue
                
                if i+1 >= l:
                    return None
                
                return q[i+1]

            temp = []
            for node in q:
                if node.left:
                    temp.append(node.left)

                if node.right:
                    temp.append(node.right)

            q = temp

        return None