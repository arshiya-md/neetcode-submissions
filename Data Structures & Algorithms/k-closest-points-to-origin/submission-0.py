class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # For each point -> calculates its ecludian distance from origin
        # sqrt((x2 - x1)**2 + (y2 - y1)**2)
        # We only need to know the closest point so we can ignore sqaure root and just calculte (x2 - x1)^2 + (y2 - y1)^2 -> e.g. sqrt(4) < sqrt(5) there for comparing just 4 nd 5 is enough to know least value
        # as x1 and y1 in this problem are origin they are always 0, 0
        # Therefore formula now is -> x2**2 + y2**2
        res = []
        distances = []
        for p in points:
            dist = p[0]**2 + p[1]**2 # p[0] is x, p[1] is y
            distances.append([dist, p[0], p[1]]) # Also store the x,y (p[0], p[1]) values along with dist bcz we need to return those of the closest point

        heapq.heapify(distances) # It arranges based on first element of the list if list is a node

        while k > 0:
            dist, x, y = heapq.heappop(distances)
            res.append([x, y])
            k -= 1

        return res

        