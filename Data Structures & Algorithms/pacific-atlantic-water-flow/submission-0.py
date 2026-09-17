class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row_size = len(heights)
        col_size = len(heights[0])

        pacific_set = set()
        atlantic_set = set()

        dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        def dfs(row, col, visit, prev_height):

        ## STOP and RETURN in following cases:
            # As starting from ocean edges, visit only cells higher than the prev cell because water can only flow to current cell from higher or equal height -> current cell height must be less that prev cell height 
            # Can't visit out of the grid rows/cols
            # Skip already visted cell to avoid infinite recursion

            if (row < 0 or col < 0 or
                row >= row_size or col >= col_size or
                (row, col) in visit or
                heights[row][col] < prev_height
            ):
                return

            visit.add((row, col))

            for r, c in dir:
                dfs(row + r, col + c, visit, heights[row][col])


        # Multi-path dfs from all the edge cells

        # First column all rows -> Pacific edge
        # and Last column all rows -> Atlantic edge
        for rows in range(row_size):
            dfs(rows, 0, pacific_set, float('-inf'))
            dfs(rows, col_size - 1, atlantic_set, float('-inf'))

        # First row all columns - Pacific edge
        # and Last row all columns - Atlantic edge
        for cols in range(col_size):
            dfs(0, cols, pacific_set, float('-inf'))
            dfs(row_size - 1, cols, atlantic_set, float('-inf'))

        res = []
        for cell in pacific_set:
            if cell in atlantic_set:
                r, c = cell
                res.append([r,c])

        return res




        