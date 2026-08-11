class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False

        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            node_neighs = graph[node]
            for neigh in node_neighs:
                if neigh == parent:
                    continue
                if not dfs(neigh, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n


# {
#     0: [1],
#     1: [3],
#     3: [0],
#     2: [4]
# }

