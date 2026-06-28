class MedianFinder:

    def __init__(self):
        self.max_heap = [] # Stores smaller half of the stream
        self.min_heap = [] # Stores larger half of the stream

        
    def addNum(self, num: int) -> None:

        if self.min_heap and self.min_heap[0] <= num:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        if (len(self.min_heap) > len(self.max_heap) + 1):
            popped_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -popped_num)
            
        if (len(self.min_heap) < len(self.max_heap) - 1):
            popped_num = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -popped_num)
            

    def findMedian(self) -> float:

        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
            
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]

        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        
        