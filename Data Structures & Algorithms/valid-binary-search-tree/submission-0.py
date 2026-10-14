# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def isbst(node,leftbound,rightbound):
            if not node:
                return True
            if not(leftbound< node.val < rightbound):
                return False
            return (isbst(node.left,leftbound,node.val) and isbst(node.right,node.val,rightbound))
        return isbst(root,float('-inf'),float('inf'))