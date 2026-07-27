# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, total):
            if not node:
                return False
            
            current_total = total + node.val
            if not node.left and not node.right:
                return current_total == targetSum
            
            if dfs(node.left, current_total):
                return True
            if dfs(node.right, current_total):
                return True
            
            return False
        
        return dfs(root, 0)
