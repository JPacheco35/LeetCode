# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # wrapper function for recursion 
        def findMax(root):
            
            # Case: no node here --> 0
            if root == None:
                return 0
        
            # otherwise, reutrn 1 + max number of levels from either of the child nodes
            return 1 + max(findMax(root.left),findMax(root.right))
        
        return findMax(root)