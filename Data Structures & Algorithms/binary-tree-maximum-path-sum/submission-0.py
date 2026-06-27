# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def max_path_sum(node):
            nonlocal res
            if node is None:
                return 0

            left = max(0, max_path_sum(node.left))
            right = max(0, max_path_sum(node.right))

            res = max(res, node.val + left + right)
            
            return node.val + max(left, right)

        max_path_sum(root)
        return res

        