# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        # wrapper function for recursion 
        def findMin(root):
            
            # Case: empty tree --> return 0
            if root == None:
                return 0
            
            # Case: only left child --> 1 + left subtree
            if root.left != None and root.right == None:
                return 1 + findMin(root.left)
            
            # Case: only right child --> 1 + right subtree
            if root.left == None and root.right != None:
                return 1 + findMin(root.right)
            
            # Case: leaf node --> we end here, +1 level for this node
            if root.left == None and root.right == None:
                return 1
        
            # Case: both childs exist --> 1 + min of each subtree
            return 1 + min(findMin(root.left),findMin(root.right))
        
        return findMin(root)