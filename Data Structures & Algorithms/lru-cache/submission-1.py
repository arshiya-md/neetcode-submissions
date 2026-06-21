class Node:
    def  __init__(self, key, val, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.data = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.nxt = self.right
        self.right.prev = self.left
        
    def _remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def _insert(self, node):
        prev = self.right.prev
        prev.nxt, node.prev = node, prev
        self.right.prev, node.nxt = node, self.right

    def get(self, key: int) -> int:
        # Check for the key in data, 
        # if doesn't exists return -1
        # else remove it from its current place and bring it to most recent side of queue
        # return the value

        if key not in self.data:
            return -1
        self._remove(self.data[key])
        self._insert(self.data[key])
        return self.data[key].val
        

    def put(self, key: int, value: int) -> None:
        # Create node and add it to respective key in the data
        # If key already exists then remove it from its current pos in the recency list
        # Add the new node to the most recent side of queue
        # Check the size of current data
        # If exceeded the capacity, remove least recently used item (left most item) 
        # from recency queue and then the data

        if key in self.data:
            self._remove(self.data[key])
        self.data[key] = Node(key, value)
        self._insert(self.data[key])

        if len(self.data) > self.cap:
            lru = self.left.nxt
            self._remove(lru)
            del self.data[lru.key]
