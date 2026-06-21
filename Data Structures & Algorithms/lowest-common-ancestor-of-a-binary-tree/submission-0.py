# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # For any node to be LCA, 
        # EITHER
        # It (lets call it 'mid') is p or q 
        # and one of its left and right tree contain p or q
        # OR 
        # it's left subtree has p and right subtree has q or vice versa

    #1  # Means mid is the LCA when:
        # 'mid and left' OR 'mid and right' OR 'left and right' is/contain p and q

    #2  # If left part has p or q or both it must return true to it's parent(mid) else false
        # If right part has p or q or both it must return true to it's parent(mid) else false
        # Or the parent (current mid) itself can be either p or q then it must return true to its immediate parent

        lca = None
        def dfs(node):

            nonlocal lca

            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            mid = node is p or node is q 

            if left + right + mid >=2: # Refer #1 above
                lca = node

            return left or right or mid # Refer #2 above
                
        dfs(root)
        return lca

        

        