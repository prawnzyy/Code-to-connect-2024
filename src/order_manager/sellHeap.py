import heapq, TreeNode

class sellHeap:
    
    def __init__(self):
        self.heap = heapq()

    def insert(self, order):
        node = TreeNode(order)
        self.heap.heappush(node)
        self.heap.heapify()
    
    def pop(self):
        item = self.heap.heappop()
        self.heap.heapify()
        return item
    
