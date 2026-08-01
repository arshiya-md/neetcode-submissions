"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node):
            if node.val in visited:
                return visited[node.val]

            copy = Node(node.val)
            visited[node.val] = copy
            for neig in node.neighbors:
                copy.neighbors.append(dfs(neig))

            return copy

        return dfs(node) if node else None

        