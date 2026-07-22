# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        q = deque([root])
        res = []

        while q:

            q_len = len(q)

            for i in range(q_len):

                curr_node = q.popleft()

                if i == q_len - 1:
                    res.append(curr_node.val)
                
                if curr_node.left: 
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
        
        return res