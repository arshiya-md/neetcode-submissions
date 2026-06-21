# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0]) # Root is constructed

        # Now now need to construct left and right of the root
        # So pass preorder and inorder representations of left and right to buildTree

        # root.left = buildTree(preorder_of_left, inorder_of_left)
        # root.right = buildTree(preorder_of_right, inorder_of_right)
        # but we dont have preorder_of_left, inorder_of_left, preorder_of_right, inorder_of_right ready
        # Prepare these first

        # inorder -> [{left_inorder},{root/mid},{right_inorder}]
        #   so, inorder_of_left = "from start to root (excl.root/mid)" 
        #   and inorder_of_right = "from root to end (excl. root/mid)"

        mid = inorder.index(preorder[0]) # We know root value, find idx using it
        inorder_of_left = inorder[:mid]
        inorder_of_right = inorder[mid+1:]
        
        # preorder -> [{root},{left_preorder},{right_preorder}]
        #   so, preorder of left starts from next element of root(idx:1) but don't knw where it ends
        #   we need to know len of left_preorder so we can know where left_preorder ends
        #   Preorder, Inorder, and Postorder of the same tree all have the same length
        #   len of inorder_of_left == len of preorder_of_left
        #   len of inorder_of_right == len of preorder_of_right
        #   We already formed inorder of left and right so we can find len easily 
        #   and that will be same for preorder too

        # Lenght(inorder[: mid]) == mid
        # Because, len of list till any idx(excl that idx) in a list == that idx value; 
        # e.g. indices: 0,1,2,3,4,5 -> len of the sublist before idx 3 is 3 [0,1,2], len of sublist before 4 is 4 [0,1,2,3])

        preorder_of_left = preorder[1: mid+1]
        preorder_of_right = preorder[mid+1:]

        root.left = self.buildTree(preorder_of_left, inorder_of_left)
        root.right = self.buildTree(preorder_of_right, inorder_of_right)

        return root




        