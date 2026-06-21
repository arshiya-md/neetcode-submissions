# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        def tree_height(node): # Returns tree's height from given node

            if node is None:
                return 0

            left_height = tree_height(node.left)
            right_height = tree_height(node.right)

            curr_diameter = left_height + right_height # We need diameter not height

            self.diameter = max(self.diameter, curr_diameter)

            return 1 + max(left_height, right_height) # tree height

        tree_height(root)
        return self.diameter

        