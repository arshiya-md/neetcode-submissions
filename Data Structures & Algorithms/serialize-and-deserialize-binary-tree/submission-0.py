# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        encoded = []
        def dfs(node):
            if not node:
                encoded.append('N')
                return                
            encoded.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(encoded)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        data_list = data.split(",")
        self.i = 0

        def dfs():
            if data_list[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(data_list[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
            
        return dfs()

        


